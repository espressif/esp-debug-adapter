import os
import subprocess
import telnetlib
import threading
import time
from .defs import *
from . import log


class Oocd(threading.Thread):
    """
        Class to communicate to OpenOCD
    """
    CREATION_FLAGS = 0
    STDOUT_DEST = subprocess.PIPE
    GDB_PORT = 3333
    TELNET_PORT = 4444
    TCL_PORT = 6666
    chip_name = ''

    def __init__(self,
                 oocd_exec=None,
                 oocd_scripts=None,
                 oocd_cfg_files=[],
                 oocd_cfg_cmds=[],
                 oocd_debug=2,
                 oocd_args=[],
                 host='localhost',
                 log_level=None,
                 log_stream_handler=None,
                 log_file_handler=None):
        """
            Constructor.

            Parameters
            ----------
            oocd_exec : string
                path to OpenOCD executable. If None OpenOCD will not be started,
                but externally ran instance can be connected to via Telnet/TCL using 'host' argument.
            oocd_scripts : string
                path to OpenOCD scripts dir.
            oocd_cfg_files : list
                list of paths to config files. Relative to 'oocd_scripts'.
            oocd_cfg_cmds : list
                list of config commands to execute during initialization.
            oocd_debug : int
                OpenOCD debug level: 1..3.
            oocd_args : list
                list of arbitrary OpenOCD command line arguments.
            host : string
                host to connect to running OpenOCD Telnet/TCL console.
            log_level : int
                logging level for this object. See logging.CRITICAL etc
            log_stream_handler : logging.Handler
                Logging stream handler for this object.
            log_file_handler : logging.Handler
                Logging file handler for this object.
        """
        if oocd_exec is None:
            oocd_exec = os.environ.get("OPENOCD_BIN", "openocd"),
        oocd_full_args = []
        if oocd_scripts is None:
            oocd_scripts = os.environ.get("OPENOCD_SCRIPTS", None)
        if oocd_scripts is not None:
            oocd_full_args += ['-s', oocd_scripts]
        for c in oocd_cfg_cmds:
            oocd_full_args += ['-c', "'%s'" % c]
        for f in oocd_cfg_files:
            oocd_full_args += ['-f', '%s' % f]
        oocd_full_args += ['-d%d' % oocd_debug]
        oocd_full_args += oocd_args

        super(Oocd, self).__init__()
        self.do_work = True
        self._logger = log.logger_init('OpenOCD', log_level, log_stream_handler, log_file_handler)
        if oocd_exec is not None:
            # start OpenOCD
            self._logger.debug('Start OpenOCD: {%s}', oocd_full_args)
            try:
                self._oocd_proc = subprocess.Popen(
                    bufsize=0, args=[oocd_exec] + oocd_full_args,
                    stdin=None, stdout=self.STDOUT_DEST, stderr=subprocess.STDOUT,
                    creationflags=self.CREATION_FLAGS, universal_newlines=True
                )
                time.sleep(1)
            except FileNotFoundError:
                self._logger.error("OpenOCD exec file is not found!")
                raise FileNotFoundError("OpenOCD exec file is not found!")
            if self._oocd_proc.poll() is not None:
                self._logger.error("Failed to start telnet connection with OpenOCD cause it's closed!")
                self._logger.error(self._oocd_proc.stdout.read())
                raise RuntimeError("OpenOCD is closed!")
        # Open telnet connection to it
        self._logger.debug('Open telnet conn to "%s"...', host)
        try:
            self._tn = telnetlib.Telnet(host, self.TELNET_PORT, 5)
            self._tn.read_until(b'>', 5)
        except Exception as e:
            self._logger.error('Failed to open telnet connection with OpenOCD (%s)!', e)
            if e is EOFError and oocd_exec is not None:
                if self._oocd_proc.stdout:
                    out = self._oocd_proc.stdout.read()
                    self._logger.debug(
                        '================== OOCD OUTPUT START =================\n'
                        '%s================== OOCD OUTPUT END =================\n',
                        out)
                self._oocd_proc.terminate()
            raise e

    def run(self):
        while self._oocd_proc.stdout and self.do_work:
            ln = self._oocd_proc.stdout.readline()
            if len(ln) == 0:
                break
            self._logger.debug(ln.rstrip(' \r\n'))

    def stop(self):
        self._logger.debug('Close telnet conn')
        self._tn.close()
        self._logger.debug('Stop OpenOCD')
        self.do_work = False
        self._oocd_proc.terminate()
        self._logger.debug('Join thread')
        self.join()
        self._logger.debug('Close stdout')
        if self._oocd_proc.stdout:
            self._oocd_proc.stdout.close()
        self._logger.debug('OOCD thread stopped')

    def cmd_exec(self, cmd):
        # read all output already sent
        resp = self._tn.read_very_eager()
        self._logger.debug('TELNET <-: %s' % resp)
        self._logger.debug('TELNET ->: %s' % cmd)
        cmd_sent = cmd + '\n'
        cmd_sent = cmd_sent.encode('utf-8')
        self._tn.write(cmd_sent)
        resp = self._tn.read_until(b'>')
        # remove all '\r' first
        resp = resp.replace(b'\r', b'')
        # command we sent will be echoed back - remove it
        index_start = resp.find(cmd_sent)
        if index_start >= 0:
            resp = resp[index_start + len(cmd_sent):]
        # the response will also include '>', next prompt - remove it as well
        index_end = resp.rfind(b'>')
        if index_end >= 0:
            resp = resp[:index_end]
        self._logger.debug('TELNET <-: %s' % resp)
        return resp.decode('utf-8')
