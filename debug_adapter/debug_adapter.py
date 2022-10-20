# MIT License
#
# Copyright (c) 2020 Espressif Systems (Shanghai) Co. Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# SPDX-License-Identifier: MIT

import copy
import os
import os.path
import socket
import tempfile
import threading
from base64 import b64encode
from datetime import datetime

# noinspection PyCompatibility
from queue import Queue
from typing import List, Any, IO, AnyStr
from pprint import pformat

from . import debug_backend as dbg
from . import log
from .command_processor import CommandProcessor
from .internal_classes import DaOpenOcdModes, DaDevModes, DaVariableReference, DaRunState, DaStates, DaArgs
from .threads import ReaderThread, WriterThread
from .tools import sys, PY2, ObjFromDict, WIN32, path_disassemble

A2VSC_STARTED_STRING = "DEBUG_ADAPTER_STARTED"
A2VSC_READY2CONNECT_STRING = "DEBUG_ADAPTER_READY2CONNECT"
A2VSC_STOPPED_STRING = "DEBUG_ADAPTER_STOPPED"


class DebugAdapter:
    """
    Adapter class
    """

    def __init__(self, args, gdb_inst=None, oocd_inst=None):
        """
        Parameters
        ----------
        args : DaArgs
        gdb_inst : dbg.Gdb
            if provided an existing instance, handling at start_gdb()
        oocd_inst : dbg.Oocd
            if provided an existing instance, handling at start_oocd()
        """
        # === arguments adaptation
        if isinstance(args, dict):
            args = ObjFromDict(args)  # type: DaArgs

        self.start_time = datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
        log.init(args, start_time_str=self.start_time, da_inst=self, no_debug_console=args.log_no_debug_console)
        if args.debug > 2:
            log.info_no_con("Working directory: %s" % os.getcwd())
            log.info_no_con("Arguments: \n" + pformat(args.get_dict(), indent=4))

        self.args = args
        _, self.target_triple = os.path.split(args.toolchain_prefix)
        if self.target_triple.endswith('-'):
            self.target_triple = self.target_triple[:-1]

        self.socket_server = None  # type: socket.socket
        self.socket_client = None  # type: socket.socket
        self.socket_client_file = None  # type: IO[AnyStr]

        self.state = DaStates()  # type: DaStates

        # === private stuff:
        self.__write_queue = Queue()
        self._cmd_exec = CommandProcessor(self, self.__write_queue, self.args)
        self.__read_from = None
        self.__write_to = None
        self.__data_bps = {}
        self.__source_bps = {}
        self.__instr_bps = {}
        self.__threads_lock = threading.Lock()
        self.__threads = []  # type: List
        # === protected stuff
        self._gdb = gdb_inst  # type: dbg.GdbEspXtensa or dbg.Gdb
        self._oocd = oocd_inst  # type: dbg.Oocd
        # === public stuff:
        self.reader = None  # type: Any(ReaderThread,None)
        self.writer = None  # type: Any(WriterThread,None)
        self.target_poller = None  # type: Any(threading.Timer,None)
        self.thread_selected = None  # type: Any(int,None)
        self.frame_id_selected = None  # type: Any(int,None)

    def _wait_for_connection(self):
        """
        Starts listen to socket. After the connection creates file for data reading and writing
        """
        self._start_socket_listening()
        log.debug("Got connection")
        self.socket_client_file = self.socket_client.makefile('rwb')
        self.__write_to = self.socket_client_file
        self.__read_from = self.socket_client_file

    def _start_socket_listening(self):
        try:
            self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket_server.settimeout(.3)
            self.socket_server.bind(('localhost', self.args.port))
            self.socket_server.listen(0)

            log.info("Listening on port " + str(self.args.port))
            self.log_cmd(A2VSC_READY2CONNECT_STRING)
            self.state.general_state = DaRunState.READY_TO_CONNECT
            # this while is needed to make the adapter responsive to Ctrl+C during waiting for a connection.
            while (self.state.general_state >= 0):  # negative values are indicating the termination process
                try:
                    self.socket_client, _ = self.socket_server.accept()
                    break
                except socket.timeout:
                    pass
        except Exception as e:
            log.warning("Error with a port #%d" % self.args.port)
            raise e

    def get_backtrace(self, thread_id):
        """
        Send stack-list-frames to gdb
        Parameters
        ----------
        thread_id: int
            Unique thread id than could be generated with self.frame_id_create

        Returns
        -------
        str
            string with result
        """
        self._gdb.select_thread(thread_id)
        return self._gdb.get_backtrace()

    def adapter_run(self, gdb_inst=None, oocd_inst=None):
        """
        Parameters
        ----------
        gdb_inst : dbg.Gdb
            if provided an existing instance, handling at
            command_processor().on_initialize_request -> self.da.adapter_init() -> start_gdb()
        oocd_inst : dbg.Oocd
            if provided an existing instance, handling at
            command_processor().on_initialize_request -> self.da.adapter_init() -> start_oocd()

        """
        self._gdb = gdb_inst
        self._oocd = oocd_inst
        log.info('Starting. Cmd: %s\n' % (' '.join(sys.argv), ))
        self.adapter_connect()
        if self.state.general_state >= DaRunState.CONNECTED:
            self.reader.start()
            self.writer.start()
            self.state.general_state = DaRunState.RUNNING
        else:
            self.state.error = True
            log.debug('Not connected')

    def output(self, msg, category=None, source=None, line=None):
        self._cmd_exec.generate_OutputEvent(output=str(msg) + '\n', category=category, source=source, line=line)

    @staticmethod
    def log_cmd(cmd_string):
        """
        Logging method for interfacing with supervisor that monitors the log. E.g. could indicate that DA is ready
        Parameters
        ----------
        cmd_string : str
        """
        print(cmd_string)
        log.cmd("Debug adapter -> Extension: " + cmd_string)

    @staticmethod
    def frame_id_generate(thread_id, frame_level):
        """
        Codder of an unique frame id name (used dec)

        Parameters
        ----------
        thread_id : int or str
        frame_level : int or str

        Returns
        -------
        frame_id : int
        """
        frame_id = int(thread_id) * 1000 + int(frame_level)
        return frame_id

    @staticmethod
    def frame_id_read(frame_id):
        """
        DeCodder of an unique frame id name (used dec)

        Parameters
        ----------
        frame_id : int or str

        Returns
        -------
        threadId : int
        frame_level : int
        """
        frame_id = int(frame_id)
        thread_id = frame_id // 1000  # type: int
        frame_level = frame_id - thread_id * 1000
        return thread_id, frame_level

    def adapter_restart(self):  # TODO think about removing
        old_reader = self.reader
        old_writer = self.writer

        self.adapter_run()

        old_writer.request_stop = True
        old_reader.request_stop = True

        if self.args.oocd_mode == DaOpenOcdModes.RUN_AND_CONNECT:
            self.stop_oocd()
        self.stop_gdb()

    def adapter_stop(self):
        """
        Safely stops all processes of DA
        """
        log.debug('Adapter is Stopping...')
        self.state.general_state = DaRunState.STOP_PREPARATION

        try:
            log.debug('Stopping target poller')
            self.stop_target_poller()
            self.target_poller = None
        except Exception as e:
            log.warning(e)

        log.debug('Closing the GDB process')
        self.stop_gdb()

        if self.args.oocd_mode == DaOpenOcdModes.RUN_AND_CONNECT:
            log.debug('Closing the OpenOCD process')
            self.stop_oocd()

        log.debug('Closing the Socket')
        self.socket_server.close()

        try:
            log.debug('Stopping of the Writer thread')
            self.writer.stop(blocking=True)
            self.writer = None
        except Exception as e:
            log.warning(e)

        try:
            log.debug('Stopping of the Reader thread')
            self.reader.stop(blocking=True)
            self.reader = None
        except Exception as e:
            log.warning(e)

        self.state.general_state = DaRunState.STOPPED
        log.debug('Adapter is Stopped')
        self.log_cmd(A2VSC_STOPPED_STRING)

    def adapter_connect(self):
        if self.state.general_state < DaRunState.CONNECTED:
            if self.args.port is not None:
                self._wait_for_connection()
            else:
                if PY2:
                    self.__write_to = sys.stdout
                    self.__read_from = sys.stdin
                    if WIN32:
                        # must read streams as binary on windows
                        import msvcrt
                        msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
                        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
                else:
                    self.__write_to = sys.stdout.buffer
                    self.__read_from = sys.stdin.buffer
            self.reader = ReaderThread(self.__read_from, self._cmd_exec)
            self.writer = WriterThread(self.__write_to, self.__write_queue)
            self.state.general_state = DaRunState.CONNECTED
        else:
            log.debug('Already connected')

    def adapter_init(self):
        """
        Starts OpenOCD (depends on input arguments) and Gdb
        """
        if self.args.oocd_mode == DaOpenOcdModes.RUN_AND_CONNECT:
            self.start_oocd()  # will raise exception in case of error
        if self.args.developer_mode != DaDevModes.CON_CHECK:
            try:
                self.start_gdb()
            except Exception as e:
                if self.args.oocd_mode == DaOpenOcdModes.RUN_AND_CONNECT:
                    self.stop_oocd()
                raise e
        self.state.general_state = DaRunState.INITIALIZED

    def reset(self):
        """
        Reset the target and wait a stop

        Returns
        -------
        stop reason : int

        """
        self._gdb.target_reset()
        rsn = self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 10)
        return rsn

    def fw_write(self):
        """
        Writes program to target
        """
        state, rsn = self._gdb.get_target_state()
        if state != dbg.TARGET_STATE_STOPPED:
            self._gdb.exec_interrupt()
            self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 5)
        win_drive, path, name, extension, exists = path_disassemble(self.args.elfpath)
        bin_path = os.path.join(win_drive, path, name + ".bin")
        bin_path = str(bin_path)
        self._gdb.target_program(file_name=bin_path, off=self.args.app_flash_off)
        self._gdb.target_reset()
        log.debug("App was flashed\n")

    def gdb_restart(self):
        """
        Stops than starts gdb process with the same settings
        """
        self.stop_target_poller()
        self.stop_gdb()
        self._gdb = None
        self.start_gdb()
        old_bps = self.__source_bps
        self.__source_bps = {}
        for src in old_bps:
            for bpnum in old_bps[src]:
                line, cond = old_bps[src][bpnum]
                self.source_break_add(src, line, cond)

    def pause(self):
        """
        Sent an interrupt signal to target
        """
        state, rsn = self._gdb.get_target_state()
        log.debug("Target state %d" % state)
        if state != dbg.TARGET_STATE_STOPPED:
            self._gdb.exec_interrupt()
            rsn = self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 5)
        log.debug("Reason of pause: " + str(rsn))

    def select_frame(self, frame_id, force=False):
        """
        Parameters
        ----------
        frame_id : int or str
            Frame id in a format 0dTFFF where thousands is  thread number, FFF - frame level = 0...999
        force : bool
        """
        # if there is some frame_id
        if (frame_id is not None) \
                and (self.frame_id_selected != frame_id or force):  # if it is new or forced
            thread_id, fr_level = self.frame_id_read(frame_id)
            self._gdb.select_thread(thread_id)
            self._gdb.select_frame(fr_level)
            self.frame_id_selected = frame_id

    def get_scopes(self, frame_id=None):
        """

        Parameters
        ----------
        frame_id : int
            Frame number tthat could be created or read with self.frame_id_* api

        Returns
        -------
        list
            list of variable names
        """
        self.select_frame(frame_id)
        s = []
        v_list = self._gdb.get_local_variables(no_values=True)
        s.append({'name': 'Locals', 'vals_list': v_list, 'var_ref': DaVariableReference.LOCALS, 'p_hint': 'locals'})
        reg_list = self.get_registers()
        s.append({'name': 'Registers', 'vals_list': reg_list,
                  'var_ref': DaVariableReference.REGISTERS, 'p_hint': 'registers'})
        return s

    def get_vars(self, frame_id=None):
        """
        List of variables. Each variable is an object in terms of GDB (read the manual)

        Parameters
        ----------
        frame_id : int
            Frame number tthat could be created or read with self.frame_id_* api

        Returns
        -------
            list
                list of local variables

        """
        self.select_frame(frame_id, force=True)  # TODO try to remove changing of a frame
        v = self._gdb.get_local_variables(no_values=False)
        return v

    def get_registers(self):
        """
        List of registers. Each register host a value in hex.

        Parameters
        ----------
        fmt: string
            Format to use for registers

        Returns
        -------
            list
                list of registers
        """
        r_names_list = self._gdb.get_reg_names()
        r_values_list = self._gdb.get_reg_values('x')
        reg_list = []

        for reg_val in r_values_list:
            reg_list.append({'name': r_names_list[int(reg_val['number'])],
                             'value': reg_val['value'], 'ref': int(reg_val['number'])})
        return reg_list

    def inst_break_add(self, addr, condition=''):
        """
        Instruction Breakpoint setting

        Parameters
        ----------
        addr : str
        condition : str
        """
        bp_num = self._gdb.add_bp("*{}".format(addr), ignore_count=0, cond=condition)
        if addr not in self.__instr_bps:
            self.__instr_bps[addr] = {}
        assert bp_num not in self.__instr_bps[addr]
        self.__instr_bps[addr][bp_num] = (addr, condition)
        return bp_num

    def inst_break_removeall(self):
        for addr in self.__instr_bps:
            for bp_num in self.__instr_bps[addr]:
                self._gdb.delete_bp(bp_num)
            self.__instr_bps.pop(addr)

    def source_break_add(self, src, line, condition=''):
        """
        Breakpoint setting

        Parameters
        ----------
        condition : str
        src : str
        line : int
        """
        bp_num = self._gdb.add_bp("{}:{}".format(src, line), ignore_count=0, cond=condition)
        if src not in self.__source_bps:
            self.__source_bps[src] = {}
        assert bp_num not in self.__source_bps[src]
        self.__source_bps[src][bp_num] = (line, condition)
        return bp_num

    def source_break_removeall(self, source_path):
        if source_path not in self.__source_bps:
            return
        for bp_num in self.__source_bps[source_path]:
            self._gdb.delete_bp(bp_num)
        self.__source_bps.pop(source_path)

    def data_break_add(self, expr, accessType='write'):
        """
        Data breakpoint setting

        Parameters
        ----------
        exp : str
        tp : str
        """
        tp = 'w'
        if accessType == 'read':
            tp = 'r'
        elif accessType == 'readWrite':
            tp = 'rw'
        bp_num = self._gdb.add_wp(expr, tp)
        assert bp_num not in self.__data_bps
        self.__data_bps[bp_num] = expr
        return bp_num

    def data_break_removeall(self):
        for bp_num in self.__data_bps.keys():
            self._gdb.delete_bp(bp_num)
        self.__data_bps.clear()

    def _gdb2dap_reason(self, rsn):
        if rsn == dbg.TARGET_STOP_REASON_BP:
            frame = self._gdb.get_current_frame()
            if frame['addr'] in self.__instr_bps:
                return 'instruction breakpoint'
            else:
                return 'breakpoint'
        elif rsn == dbg.TARGET_STOP_REASON_STEPPED:
            return 'stepped'
        elif rsn == dbg.TARGET_STOP_REASON_SIGINT:
            return 'pause'
        elif rsn == dbg.TARGET_STOP_REASON_SIGTRAP:
            return 'data breakpoint'
        elif rsn == dbg.TARGET_STOP_REASON_FN_FINISHED:
            return 'entry'
        else:
            return 'exception'

    def is_stopped(self):
        """
        Returns
        -------
        bool
            True - stopped, False - not.
        int
            The reason of stopping
        """
        try:
            r = self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 0)
            return True, r
        except dbg.DebuggerTargetStateTimeoutError:
            return False, ''

    def is_inherited_gdb(self):
        """
        Check if there is some gdb object for using instead of creating the one one by DA
        Returns
        -------
        bool
            Result
        """
        return self._gdb is not None

    def is_inherited_oocd(self):
        """
        Check if there is some openocd object for using instead of creating the one one by DA
        Returns
        -------
        bool
            Result
        """
        return self._oocd is not None

    def start_gdb(self):  # noqa: C901
        """
        Starting GDB and write the result into state.gdb_started attribute
        """
        if not self.is_inherited_gdb():
            try:
                if log.CGF_LOG_TO_MULT_FILES:
                    log_file_handler = log.get_file_handler('adapter_gdb_')
                else:
                    log_file_handler = log.get_file_handler()
                if self.args.oocd_mode == DaOpenOcdModes.NO_OOCD:
                    remote_target = ""  # to not connect to anything
                else:
                    remote_target = None  # for the default value

                gdb_path = None  # default GDB path will be used
                if len(self.args.toolchain_prefix):
                    # assume GDB path basing on toolchain prefix
                    gdb_path = "{}gdb".format(self.args.toolchain_prefix)
                self._gdb = dbg.create_gdb(chip_name=self.args.device_name,
                                           target_triple=self.target_triple,
                                           gdb_path=gdb_path,
                                           log_level=log.level,
                                           log_file_handler=log_file_handler,
                                           log_stream_handler=log.stream_handler,
                                           gdb_log_file=os.path.join(tempfile.gettempdir(), "gdb_proc.log"),
                                           remote_target=remote_target)
                log.debug("Created gdb object of type: %s" % self._gdb.__class__.__name__)
                self._gdb.tmo_scale_factor = self.args.tmo_scale_factor
                if isinstance(self.args.elfpath, str):
                    self._gdb.exec_file_set(self.args.elfpath)
                else:
                    for elf in self.args.elfpath:
                        self._gdb.exec_file_set(elf)
                if isinstance(self.args.core_file, str):
                    self._gdb.exec_file_core_set(self.args.core_file)
                else:
                    for core in self.args.core_file:
                        self._gdb.exec_file_core_set(core)
                if self.args.cmdfile:
                    self._gdb.set_prog_startup_script(self.args.cmdfile)
                if not self.args.postmortem:
                    self._gdb.connect()
                self._gdb.app_flash_offset = self.args.app_flash_off
            except Exception as e:
                raise e
        self.state.gdb_started = True

    def start_oocd(self):
        """ Starts oocd, write the result into state.oocd_started attribute
        """
        if not self.args.oocd:
            return
        if not self.is_inherited_oocd():
            # if self.args.debug > 4: # TODO doesn't connecting with this
            #     oocd_args = oocd_args + ['-d']
            if log.CGF_LOG_TO_MULT_FILES:
                log_file_handler = log.get_file_handler('adapter_oocd_')
            else:
                log_file_handler = log.get_file_handler()
            self._oocd = dbg.create_oocd(chip_name=self.args.device_name,
                                         target_triple=self.target_triple,
                                         oocd_exec=self.args.oocd,
                                         oocd_scripts=self.args.oocd_scripts,
                                         oocd_args=self.args.oocd_args,
                                         host=self.args.oocd_ip,
                                         log_level=log.level,
                                         log_file_handler=log_file_handler,
                                         log_stream_handler=log.stream_handler)
            self._oocd.start()
            self.state.oocd_started = True

    def stop_oocd(self):
        """
        Stops OpenOCD subprocess if it was launched
        """
        try:
            if self.state.oocd_started:
                self._oocd.stop()
                self.state.oocd_started = False
        except Exception as e:
            log.debug(e)

    def stop_gdb(self):
        """
        Stops GDB subprocess if it was lauched
        """
        try:
            if self.state.gdb_started:
                self._gdb.gdb_exit()
                self.state.gdb_started = False
        except Exception as e:
            log.debug(e)

    def on_target_stopped(self, rsn):
        self.update_threads()
        self._cmd_exec.generate_StoppedEvent(reason=self._gdb2dap_reason(rsn),
                                             thread_id=int(self.thread_selected),
                                             all_threads_stopped=self.state.threads_are_stopped)

    def start_target_poller(self, state):
        self.state.wait_target_state = state
        self.target_poller = threading.Timer(0.1, self.poll_target, args=[
            self,
        ])
        self.target_poller.start()

    def stop_target_poller(self):
        self.state.wait_target_state = dbg.TARGET_STATE_UNKNOWN
        if self.target_poller and self.target_poller.is_alive():
            self.target_poller.cancel()
            self.target_poller.join()

    def poll_target(self, *kwargs):
        log.debug("Poll target. Wait state %s" % self.state.wait_target_state)
        if self.state.wait_target_state == dbg.TARGET_STATE_STOPPED:
            stopped, rsn = self.is_stopped()
            if stopped:
                self.on_target_stopped(rsn)
                self.state.wait_target_state = dbg.TARGET_STATE_UNKNOWN
        elif self.state.wait_target_state == dbg.TARGET_STATE_RUNNING:
            # this is not fully implemented yet, need to define when we need to start waiting for target get running
            try:
                self._gdb.wait_target_state(dbg.TARGET_STATE_RUNNING, 0)
                self._cmd_exec.generate_ContinuedEvent(thread_id=0, all_threads_continued=True)
                self.state.wait_target_state = dbg.TARGET_STATE_UNKNOWN
            except dbg.DebuggerTargetStateTimeoutError:
                pass
        if self.state.wait_target_state != dbg.TARGET_STATE_UNKNOWN:
            log.debug("Poll target restart")
            # restart timer if we still need to wait for target state
            self.target_poller = threading.Timer(0.1, self.poll_target, args=[
                self,
            ])
            self.target_poller.start()

    def get_thread_list(self):
        with self.__threads_lock:
            # return a copy of list because thread list can be modified asynchronously by other execution threads
            return copy.deepcopy(self.__threads)

    def update_threads(self):
        """
        Read threads existing on target
        """
        # raise exception if target is not stopped
        # TODO: do we actually need target to be stopped?
        # self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 0)
        state, _ = self._gdb.get_target_state()
        if state != dbg.TARGET_STATE_STOPPED:
            raise RuntimeError("Can not update threads in not STOPPED mode!")
        gdb_resp = self._gdb.get_thread_info()
        # this method can be called from different execution threads:
        # main DAP request processing loop and GDB target state notifier,
        # so need to lock access to it
        with self.__threads_lock:
            self.thread_selected = int(gdb_resp[0])
            self.__threads = gdb_resp[1]
            self.state.threads_are_stopped = True
            for t in self.__threads:
                if t['state'] != "stopped":
                    self.state.threads_are_stopped = False
                    break

    def set_variable(self, name, value):
        """
        Parameters
        ----------
        name : str
            name of a variable
        value : str
        """
        # TODO: select frame is not selected?
        # self._gdb.var_assign(file_func, name, value)
        self._gdb.data_eval_expr('%s=%s' % (name, value))

    def evaluate(self, expr):
        """
        Parameters
        ----------
        expr: str

        Returns
        -------
        result: str
        """
        r = self._gdb.data_eval_expr(expr)
        return r

    def read_memory(self, addr, count, offset):
        """
        Parameters
        ----------
        addr: str
            address to read in memory
        count: int
            number of bytes to read
        offset: int
            offset from addr to read
        """
        memory_result = self._gdb.read_memory_bytes(addr, count, offset)
        mem_data = memory_result[0]['contents']
        num_bytes = len(memory_result[0]['contents']) // 2
        int_arr = [None] * num_bytes
        dx = 0
        char_int_dict = dict(zip([format(i, 'x').zfill(2) for i in range(256)], range(256)))
        for ix in range(num_bytes):
            tmp = mem_data[dx] + mem_data[dx + 1]
            dx = dx + 2
            int_arr[ix] = char_int_dict[tmp]
        bytes_from_arr = bytes(int_arr)
        encoded_base64_str = b64encode(bytes_from_arr).decode()
        return encoded_base64_str

    def gdb_execute(self, cmd):
        """

        Parameters
        ----------
        cmd :str
            Execute a console command in GDB

        Returns
        -------
        res, res_body
        """
        return self._gdb.console_cmd_run(cmd)

    def stop_exec(self):
        """ Stops target execution and ensures that it is in STOPPED state
        """
        state, _ = self._gdb.get_target_state()
        if state != dbg.TARGET_STATE_STOPPED:
            self._gdb.exec_interrupt()
            rsn = self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 10)
            assert (rsn == dbg.TARGET_STOP_REASON_SIGINT)

    def resume_exec(self, loc=None):
        """
        Resumes target execution and ensures that it is in RUNNING state

        Parameters
        ----------
        loc : str
            Location to which pc will jump before executing 'continue'
        """
        state, _ = self._gdb.get_target_state()
        if state != dbg.TARGET_STATE_RUNNING:
            if loc:
                log.debug('Resume from addr 0x%x' % int(loc))
                self._gdb.exec_jump(loc)
            else:
                self._gdb.exec_continue()
            self._gdb.wait_target_state(dbg.TARGET_STATE_RUNNING, 5)
        self.start_target_poller(dbg.TARGET_STATE_STOPPED)

    def run(self, start=False):
        """
        Runs a target program execution. If start==True set breakpoint at main_func if specified
        """
        state, _ = self._gdb.get_target_state()
        if state == dbg.TARGET_STATE_RUNNING:
            self.pause()
        if self.args.postmortem:
            # do not run in postmortem mode, just update threads list
            self.update_threads()
        else:
            if self.args.cmdfile:  # if a custom startup file specified, execute only it
                self._gdb.exec_run(only_startup=True, startup_tmo=5)
            else:
                self._gdb.exec_run()
            if start:
                rsn = self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED, 10)
                self.on_target_stopped(rsn)

    def start(self):
        self.run(start=True)

    def _check_run_n_stop(self):
        try:
            self._gdb.wait_target_state(dbg.TARGET_STATE_RUNNING)
            self._gdb.wait_target_state(dbg.TARGET_STATE_STOPPED)
            pass
        except dbg.DebuggerTargetStateTimeoutError:
            return False
        return True

    def step(self):
        """
        Performs program step (step over, "next" command in GDB)
        """
        # self._gdb.get_current_frame()
        self._gdb.exec_next()
        return self._check_run_n_stop()

    def step_in(self):
        """
        Performs program step (step in, "step" command in GDB)
        """
        self._gdb.exec_step()
        return self._check_run_n_stop()

    def step_out(self):
        """
        Runs until current function returns (step out, "finish" command in GDB)
        """
        self._gdb.exec_finish()
        return self._check_run_n_stop()

    def get_disassemble_instructions(self, start_addr, end_addr):
        """
        Return disassembled instructions from a given address range

        Parameters
        ----------
        start_addr ; int
            initial address to read

        end_addr : int
            end address to read

        Returns
        -------
        list
            List of disassemble instructions
        """
        errs = 0
        instructions = []
        mode = 5  # Disassemble mode 5 to include C code
        try:
            val = self._gdb.disassemble(start_addr, end_addr, mode)
            for inst in val:
                line = inst['line'] if 'line' in inst else None
                source = {
                    'name': inst['file'] if 'file' in inst else None,
                    'path': inst['fullname'] if 'fullname' in inst else None
                }
                for asm_line in inst['line_asm_insn']:
                    new_instruction = {
                        "address": asm_line['address'],
                        "instruction": asm_line['inst'],
                        "instructionBytes": asm_line['opcodes'] if 'opcodes' in asm_line else None,
                        "line": line,
                        "location": source
                    }
                    instructions.append(new_instruction)
        except TypeError:
            errs += 1
        return (instructions, errs)
