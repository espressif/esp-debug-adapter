from . import log
from .defs import *
import os
import time
import re
import threading
from pprint import pformat
from pygdbmi.gdbcontroller import GdbController


class Gdb(object):
    """
        Class to communicate to GDB
    """
    chip_name = ''

    def __init__(self, gdb_path='gdb',
                 remote_target=None,
                 extended_remote_mode=False,
                 gdb_log_file=None,
                 log_level=None,
                 log_stream_handler=None,
                 log_file_handler=None):
        """
            Constructor.

            Parameters
            ----------
            gdb_path : string
                path to GDB executable.
            remote_target : string
                remote target address, for possible values see https://www.sourceware.org/gdb/onlinedocs/gdb/Connecting.html.
                Should be None for local targets.
            extended_remote_mode : bool
                If True extended remote mode should be used.
            gdb_log_file : string
                path to GDB log file.
            log_level : int
                logging level for this object. See logging.CRITICAL etc
            log_stream_handler : logging.Handler
                Logging stream handler for this object.
            log_file_handler : logging.Handler
                Logging file handler for this object.
        """
        self.main_func = 'main'
        self._remote_target = remote_target
        self._extended_remote_mode = extended_remote_mode
        self._logger = log.logger_init("Gdb", log_level, log_stream_handler, log_file_handler)
        self._gdbmi = GdbController(gdb_path=gdb_path)
        self._gdbmi_lock = threading.Lock()
        self._resp_cache = []
        self._target_state = TARGET_STATE_UNKNOWN
        self._target_stop_reason = TARGET_STOP_REASON_UNKNOWN
        self.stream_handlers = {'console': None, 'target': None, 'log': None}
        self._curr_frame = None
        self._curr_wp_val = None
        # gdb config
        self.gdb_set("mi-async", "on")
        if gdb_log_file is not None:
            pardirs = os.path.dirname(gdb_log_file)
            if pardirs:
                os.makedirs(pardirs, exist_ok=True)  # create non-existing folders
            self.gdb_set("logging", "file %s" % gdb_log_file)
            self.gdb_set("logging", "on")

    def _on_notify(self, rec):
        if rec['message'] == 'stopped':
            self._target_state = TARGET_STATE_STOPPED
            self._curr_frame = rec['payload']['frame']
            if 'reason' in rec['payload']:
                if rec['payload']['reason'] == 'breakpoint-hit':
                    self._target_stop_reason = TARGET_STOP_REASON_BP
                elif rec['payload']['reason'] == 'watchpoint-trigger':
                    self._target_stop_reason = TARGET_STOP_REASON_WP
                    self._curr_wp_val = rec['payload']['value']
                elif rec['payload']['reason'] == 'watchpoint-scope':
                    self._target_stop_reason = TARGET_STOP_REASON_WP_SCOPE
                elif rec['payload']['reason'] == 'end-stepping-range':
                    self._target_stop_reason = TARGET_STOP_REASON_STEPPED
                elif rec['payload']['reason'] == 'function-finished':
                    self._target_stop_reason = TARGET_STOP_REASON_FN_FINISHED
                elif rec['payload']['reason'] == 'signal-received':
                    if rec['payload']['signal-name'] == 'SIGINT':
                        self._target_stop_reason = TARGET_STOP_REASON_SIGINT
                    elif rec['payload']['signal-name'] == 'SIGTRAP':
                        self._target_stop_reason = TARGET_STOP_REASON_SIGTRAP
                    else:
                        self._logger.warning('Unknown signal received "%s"!', rec['payload']['signal-name'])
                        self._target_stop_reason = TARGET_STOP_REASON_UNKNOWN
                else:
                    self._logger.warning('Unknown target stop reason "%s"!', rec['payload']['reason'])
                    self._target_stop_reason = TARGET_STOP_REASON_UNKNOWN
            else:
                self._target_stop_reason = TARGET_STOP_REASON_UNKNOWN
        elif rec['message'] == 'running':
            self._target_state = TARGET_STATE_RUNNING

    def _parse_mi_resp(self, new_resp, new_tgt_state):
        result = None
        result_body = None
        old_state = self._target_state
        # if any cached records go first
        resp = self._resp_cache + new_resp
        processed_recs = 0
        for rec in resp:
            processed_recs += 1
            if rec['type'] == 'log':
                self._logger.debug('LOG: %s', pformat(rec['payload']))
                if self.stream_handlers['log']:
                    self.stream_handlers['log'](rec['payload'])
            elif rec['type'] == 'console':
                self._logger.info('CONS: %s', pformat(rec['payload']))
                if self.stream_handlers['console']:
                    self.stream_handlers['console'](rec['payload'])
            elif rec['type'] == 'target':
                self._logger.debug('TGT: %s', pformat(rec['payload']))
                if self.stream_handlers['target']:
                    self.stream_handlers['target'](rec['payload'])
            elif rec['type'] == 'notify':
                self._logger.info('NOTIFY: %s %s', rec['message'], pformat(rec['payload']))
                self._on_notify(rec)
                # stop upon result receiption if we do not expect target state change
                if self._target_state != old_state and self._target_state == new_tgt_state:
                    self._logger.debug('new target state %d', self._target_state)
                    break
            elif rec['type'] == 'result':
                self._logger.debug('RESULT: %s %s', rec['message'], pformat(rec['payload']))
                result = rec['message']
                result_body = rec['payload']
                # stop upon result reception if we do not expect target state change
                if not new_tgt_state:
                    break
        # cache unprocessed records
        self._resp_cache = resp[processed_recs:]
        # self._logger.debug('cached recs: %s', pformat(self._resp_cache))
        return result, result_body

    def _mi_cmd_run(self, cmd, new_tgt_state=None, tmo=5):
        def _mi_cmd_isdone(cmd, response):
            if len(response):
                # TODO: less hardcode
                if cmd in ['-exec-step', '-exec-next', '-exec-continue', '-exec-continue --all', '-exec-finish']:
                    if response[-1].get('message') == 'stopped':
                        return True
                elif cmd == '-thread-info':
                    if (response[-1].get('message') == 'done') or \
                            (len(response) > 1 and response[-2].get('message') == 'done' and
                             response[-1].get('message') == 'thread-selected'):
                        return True
            else:
                if response[-1].get('message') == 'done':
                    return True
            return False

        with self._gdbmi_lock:
            self._logger.debug('MI->: %s', cmd)
            response = []
            end = time.time()
            if tmo:
                end += tmo
                done = False
                try:
                    self._gdbmi.write(cmd, read_response=False)
                    while time.time() <= end and not done:  # while time is not up
                        r = self._gdbmi.get_gdb_response(timeout_sec=0, raise_error_on_timeout=False)
                        response += r
                        done = _mi_cmd_isdone(cmd, response)
                except Exception as e:
                    self._gdbmi.verify_valid_gdb_subprocess()
            else:
                while len(response) == 0:
                    response = self._gdbmi.write(cmd, raise_error_on_timeout=False)
            self._logger.debug('MI<-:\n%s', pformat(response))
            res, res_body = self._parse_mi_resp(response, new_tgt_state)  # None, None if empty
            while not res:
                # check for result report from GDB
                response = self._gdbmi.get_gdb_response(0, raise_error_on_timeout=False)
                if not len(response):
                    if tmo and (time.time() >= end):
                        raise DebuggerTargetStateTimeoutError(
                            'Failed to wait for completion of command "%s" / %s!' % (cmd, tmo))
                else:
                    self._logger.debug('MI<-:\n%s', pformat(response))
                    res, res_body = self._parse_mi_resp(response, new_tgt_state)  # None, None if empty
        return res, res_body

    def stream_handler_set(self, stream_type, handler):
        if stream_type not in self.stream_handlers:
            raise DebuggerError('Unsupported stream type "%s"' % stream_type)
        self.stream_handlers[stream_type] = handler

    def gdb_exit(self, tmo=5):
        """ -gdb-exit ~= quit """
        self._mi_cmd_run("-gdb-exit", tmo=tmo)

    def console_cmd_run(self, cmd, tmo=5):
        self._mi_cmd_run("-interpreter-exec console \"%s\"" % cmd, tmo=tmo)

    def target_select(self, tgt_type, tgt_params, tmo=5):
        # -target-select type parameters
        res, _ = self._mi_cmd_run('-target-select %s %s' % (tgt_type, tgt_params), tmo=tmo)
        if res != 'connected':
            raise DebuggerError('Failed to connect to "%s %s"!' % (tgt_type, tgt_params))

    def target_disconnect(self):
        # -target-disconnect
        self._mi_cmd_run('-target-disconnect')

    def target_reset(self, action='halt', tmo=5):
        self.monitor_run('reset %s' % action)
        if action == 'halt':
            self.wait_target_state(TARGET_STATE_STOPPED, tmo=tmo)
            self.console_cmd_run('flushregs')

    def exec_file_set(self, file_path):
        # -file-exec-and-symbols file
        local_file_path = file_path
        if os.name == 'nt':
            # Convert filepath from Windows format if needed
            local_file_path = local_file_path.replace("\\", "/")
        res, _ = self._mi_cmd_run('-file-exec-and-symbols %s' % local_file_path)
        if res != 'done':
            raise DebuggerError('Failed to set program file!')

    def exec_interrupt(self):
        # -exec-interrupt [--all|--thread-group N]
        res, _ = self._mi_cmd_run('-exec-interrupt --all')
        if res != 'done':
            raise DebuggerError('Failed to stop program!')

    def exec_continue(self):
        # -exec-continue [--reverse] [--all|--thread-group N]
        res, _ = self._mi_cmd_run('-exec-continue --all')
        if res != 'running':
            raise DebuggerError('Failed to continue program!')

    def exec_run(self, start=True):
        # -exec-run [ --all | --thread-group N ] [ --start ]
        if start:
            cmd = '-exec-run --all --start'
        else:
            cmd = '-exec-run --all'
        res, _ = self._mi_cmd_run(cmd)
        if res != 'running':
            raise DebuggerError('Failed to run program!')

    def exec_jump(self, loc):
        # -exec-jump location
        res, _ = self._mi_cmd_run('-exec-jump %s' % loc)
        if res != 'running':
            raise DebuggerError('Failed to make jump in program!')

    def exec_next(self):
        # -exec-next [--reverse]
        res, _ = self._mi_cmd_run('-exec-next')
        if res != 'running':
            raise DebuggerError('Failed to step over!')

    def exec_step(self):
        # -exec-step [--reverse]
        res, _ = self._mi_cmd_run('-exec-step')
        if res != 'running':
            raise DebuggerError('Failed to step in!')

    def exec_finish(self):
        # -exec-finish [--reverse]
        res, _ = self._mi_cmd_run('-exec-finish')
        if res != 'running':
            raise DebuggerError('Failed to step out!')

    def exec_next_insn(self):
        # -exec-next-instruction [--reverse]
        res, _ = self._mi_cmd_run('-exec-next-instruction')
        if res != 'running':
            raise DebuggerError('Failed to step insn!')

    def data_eval_expr(self, expr):
        # -data-evaluate-expression expr
        res, res_body = self._mi_cmd_run('-data-evaluate-expression "%s"' % expr, tmo=1)
        if res == "done" and 'value' in res_body:
            return res_body['value']
        elif res == "error" and 'msg' in res_body:
            return res_body['msg']
        else:
            raise DebuggerError('Failed to eval expression!')

    def extract_exec_addr(self, addr_val):
        sval_re = re.search('(.*)[<](.*)[>]', addr_val)
        if sval_re:
            return int(sval_re.group(1), 0)
        return int(addr_val, 0)

    def get_reg(self, nm):
        sval = self.data_eval_expr('$%s' % nm)
        # for PC we'll get something like '0x400e0db8 <gpio_set_direction>'
        return self.extract_exec_addr(sval)

    def gdb_set(self, var, val):
        res,_ = self._mi_cmd_run("-gdb-set %s %s" % (var, val))
        if res != "done":
            raise DebuggerError('Failed to set variable!')

    def get_variables(self, thread_num=None, frame_num=0):
        # -stack-list-variables [ --no-frame-filters ] [ --skip-unavailable ] print-values
        if thread_num is not None:
            cmd = '-stack-list-variables --thread %d --frame %d --all-values' % (thread_num, frame_num)
        else:
            cmd = '-stack-list-variables --all-values'
        res, res_body = self._mi_cmd_run(cmd)
        if res != 'done' or not res_body or 'variables' not in res_body:
            raise DebuggerError('Failed to get variables @ frame %d of thread %d!' % (frame_num, thread_num))
        return res_body['variables']

    def get_local_variables(self, no_values=False):
        # -stack-list-variables [ --no-frame-filters ] [ --skip-unavailable ] print-values
        # noinspection PyTypeChecker
        cmd = '-stack-list-locals %i' % int(not no_values)
        res, res_body = self._mi_cmd_run(cmd)
        if res != 'done' or not res_body or 'locals' not in res_body:
            raise DebuggerError('Failed to get variables @ frame')
        return res_body['locals']

    def get_backtrace(self):
        # -stack-list-frames [ --no-frame-filters low-frame high-frame ]
        res, res_body = self._mi_cmd_run('-stack-list-frames')
        if res != 'done' or not res_body or 'stack' not in res_body:
            raise DebuggerError('Failed to get backtrace! (%s / %s)' % (res, res_body))
        return res_body['stack']

    def select_frame(self, frame):
        # -stack-select-frame framenum
        res, _ = self._mi_cmd_run('-stack-select-frame %d' % frame)
        if res != 'done':
            raise DebuggerError('Failed to get backtrace!')

    def add_bp(self, loc, ignore_count=0, cond='', hw=False, tmp=False):
        # -break-insert [ -t ] [ -h ] [ -f ] [ -d ] [ -a ] [ -c condition ] [ -i ignore-count ]
        # [ -p thread-id ] [ location ]
        cmd_args = '-i %d %s' % (ignore_count, loc)
        if len(cond):
            cmd_args = '-c "%s" %s' % (cond, cmd_args)
        if hw:
            cmd_args = "-h " + cmd_args
        if tmp:
            cmd_args = "-t " + cmd_args
        res, res_body = self._mi_cmd_run('-break-insert %s' % cmd_args)
        if res != 'done' or not res_body or 'bkpt' not in res_body or 'number' not in res_body['bkpt']:
            raise DebuggerError('Failed to insert BP!')
        return res_body['bkpt']['number']

    def add_wp(self, exp, tp='w'):
        # -break-watch [ -a | -r ] expr
        cmd_args = '"%s"' % exp
        if tp == 'r':
            cmd_args = '-r %s' % cmd_args
        elif tp == 'rw':
            cmd_args = '-a %s' % cmd_args
        res, res_body = self._mi_cmd_run('-break-watch %s' % cmd_args)
        if res != 'done' or not res_body:
            raise DebuggerError('Failed to insert WP!')
        if tp == 'w':
            if 'wpt' not in res_body or 'number' not in res_body['wpt']:
                raise DebuggerError('Failed to insert WP!')
            return res_body['wpt']['number']
        elif tp == 'r':
            if 'hw-rwpt' not in res_body or 'number' not in res_body['hw-rwpt']:
                raise DebuggerError('Failed to insert RWP!')
            return res_body['hw-rwpt']['number']
        elif tp == 'rw':
            if 'hw-awpt' not in res_body or 'number' not in res_body['hw-awpt']:
                raise DebuggerError('Failed to insert AWP!')
            return res_body['hw-awpt']['number']
        return None

    def delete_bp(self, bp):
        # -break-delete ( breakpoint )+
        res, _ = self._mi_cmd_run('-break-delete %s' % bp)
        if res != 'done':
            raise DebuggerError('Failed to delete BP!')

    def monitor_run(self, cmd, tmo=None):
        res, resp = self._mi_cmd_run('mon %s' % cmd, tmo=tmo)
        if res != 'done':
            raise DebuggerError('Failed to run monitor cmd "%s"!' % cmd)
        return resp

    def wait_target_state(self, state, tmo=None):
        """
        Parameters
        ----------
        state : int
        tmo : int
        Returns
        -------
        stop_reason : int
        """
        with self._gdbmi_lock:
            end = time.time()
            if tmo is not None:
                end += tmo
            while self._target_state != state:
                if len(self._resp_cache):
                    recs = []#self._resp_cache
                else:
                    # check for target state change report from GDB
                    recs = self._gdbmi.get_gdb_response(0.5, raise_error_on_timeout=False)
                    if tmo and len(recs) == 0 and time.time() >= end:
                        raise DebuggerTargetStateTimeoutError("Failed to wait for target state %d!" % state)
                self._parse_mi_resp(recs, state)
        return self._target_stop_reason

    def get_target_state(self):
        return self._target_state, self._target_stop_reason

    def get_current_frame(self):
        return self._curr_frame

    def get_current_wp_val(self):
        return self._curr_wp_val

    def connect(self, tmo=5):
        self._logger.debug('Connect to %s', self._remote_target)
        if self._remote_target is None:
            return
        remote_mode = 'extended_remote' if self._extended_remote_mode else 'remote'
        self.target_select(remote_mode, self._remote_target, tmo=tmo)

    def disconnect(self):
        self.target_disconnect()

    def resume(self):
        self.exec_continue()
        self.wait_target_state(TARGET_STATE_RUNNING, 5)

    def halt(self):
        if self._target_state == TARGET_STATE_STOPPED:
            return
        self.exec_interrupt()
        self.wait_target_state(TARGET_STATE_STOPPED, 5)

    def get_thread_info(self, thread_id=None):
        """

        Parameters
        ----------
        thread_id : int or None
            thread to info if exists

        Returns
        -------
        current-thread-id : str
        threads : dict
        """
        # -thread-info [ thread-id ]
        if thread_id:
            cmd = '-thread-info %d' % thread_id
        else:
            cmd = '-thread-info'
        # streaming of info for all threads over gdbmi can take some time, so use large timeout value
        res, res_body = self._mi_cmd_run(cmd, tmo=20)
        # if res != 'done' or not res_body or 'threads' not in res_body or 'current-thread-id' not in res_body:
        if res != 'done' or not res_body or 'threads' not in res_body:  # TODO verify removing current-thread-id
            raise DebuggerError('Failed to get thread info!')
        return res_body.get('current-thread-id', None), res_body['threads']

    def select_thread(self, num):
        res, _ = self._mi_cmd_run('-thread-select %d' % num)
        if res != 'done':
            raise DebuggerError('Failed to set thread!')
        return res

    def set_thread(self, num):
        """Old-named method. For backward compatibility"""
        return self.select_thread(num)

    def get_thread_ids(self):
        # -thread-list-ids expr
        res, thread_ids = self._mi_cmd_run('-thread-list-ids')
        if res != 'done':
            raise DebuggerError('Failed to eval expression!')
        return thread_ids

    def get_selected_thread(self):
        #
        sel_id, ths = self.get_thread_info()
        for th in ths:
            if th['id'] == sel_id:
                return th
        return None

    def target_program(self):
        return None
