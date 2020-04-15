import os
from ..defs import *
from ..utils import fixup_path
from .xtensa import *


class OocdEspXtensa(OocdXtensa):
    """
        Class to communicate to OpenOCD supporting ESP Xtensa-specific features
    """

    def __init__(self, cores_num=1, oocd_exec=None, oocd_scripts=None, oocd_cfg_files=[], oocd_cfg_cmds=[],
                 oocd_debug=2, oocd_args=[], host='127.0.0.1', log_level=None, log_stream_handler=None, log_file_handler=None):
        super(OocdEspXtensa, self).__init__(oocd_exec=oocd_exec, oocd_scripts=oocd_scripts,
                                         oocd_cfg_files=oocd_cfg_files, oocd_cfg_cmds=oocd_cfg_cmds, oocd_debug=oocd_debug,
                                         oocd_args=oocd_args, host=host, log_level=log_level, log_stream_handler=log_stream_handler,
                                         log_file_handler=log_file_handler)
        self.cores_num = cores_num

    def set_appimage_offset(self, app_flash_off):
        self.cmd_exec('esp appimage_offset 0x%x' % (app_flash_off))

    def set_semihost_basedir(self, semi_dir):
        self.cmd_exec('esp semihost_basedir %s' % (fixup_path(semi_dir)))

    def gcov_dump(self, on_the_fly=True):
        if on_the_fly:
            cmd = 'esp gcov'
        else:
            cmd = 'esp gcov dump'
        self.cmd_exec(cmd)

    def sysview_start(self, file1, file2=''):
        self.cmd_exec('esp sysview start %s %s' % (file1, file2))

    def sysview_stop(self):
        self.cmd_exec('esp sysview stop')

    def perfmon_dump(self, counter = None):
        """Run OpenOCD perfmon_dump command

        Reported results are returned as a dictionary. Each key is the counter id.
        Each value is a tuple of counts for every core.
        If some CPU is disabled, its count will be None.
        """
        if self.cores_num == 1:
            # call single core version inmplementation of base class
            return {0: super(OocdEspXtensa, self).perfmon_dump(counter)}
        cmd = 'xtensa perfmon_dump'
        if counter is not None:
            cmd += ' %d' % counter
        resp = self.cmd_exec(cmd)
        # Response should have one line for every counter
        core = None
        result = {}
        lines = resp.split('\n')
        for line in lines:
            if len(line) == 0:
                continue
            tokens = re.match(r'CPU(?P<core>\d+):$', line)
            if tokens:
                core = int(tokens.group('core'))
                if core not in result:
                    result[core] = {}
            else:
                tokens = re.match(r'Counter (?P<counter>\d+): (?P<val>\d+)', line)
                val = int(tokens.group('val'))
                counter = int(tokens.group('counter'))
                result[core][counter] = val
        return result


class GdbEspXtensa(GdbXtensa):
    """
        Class to communicate to GDB supporting ESP Xtensa-specific features
    """

    def __init__(self, gdb_path, remote_target=None, extended_remote_mode=False, gdb_log_file=None,
                 log_level=None, log_stream_handler=None, log_file_handler=None):
        super(GdbEspXtensa, self).__init__(gdb_path=gdb_path, remote_target=remote_target, extended_remote_mode=extended_remote_mode,
                                        gdb_log_file=gdb_log_file, log_level=log_level, log_stream_handler=log_stream_handler,
                                        log_file_handler=log_file_handler)
        self.app_flash_offset = 0x10000 # default for for ESP xtensa chips

    def target_program(self, file_name, off, actions='verify', tmo=30):
        """

        actions can be any or both of 'verify reset'

        Parameters
        ----------
        file_name : str
        off : str
        actions : str
        tmo : int

        """
        self.monitor_run('program_esp %s %s 0x%x' % (fixup_path(file_name), actions, int(off)), tmo)

    def _update_memory_map(self):
        self.monitor_run('esp appimage_offset 0x%x' % (self.app_flash_offset), 5)
        self.disconnect()
        self.connect()

    def exec_run(self, start=True):
        """
            See Gdb.exec_run().
            WARNING: This method behaves like Gdb.exec_run().
            It does not wait for target to be stopped, just sets temp breakpoint and resumes.
        """
        self.target_reset()
        self.wait_target_state(TARGET_STATE_STOPPED, 10)
        self._update_memory_map()
        if start:
            self.add_bp(self.main_func, tmp=True)
        self.resume()

    def get_thread_info(self, thread_id=None):
        """
            See Gdb.get_thread_info().
            ESP xtensa chips need to be halted to read memory. This method stops
        """
        self.halt()
        return super(GdbEspXtensa, self).get_thread_info(thread_id)

    def gcov_dump(self, on_the_fly=True):
        if on_the_fly:
            cmd = 'esp gcov'
        else:
            cmd = 'esp gcov dump'
        self.monitor_run(cmd, tmo=30)

    def sysview_start(self, file1, file2=''):
        self.monitor_run('esp sysview start %s %s' % (file1, file2))

    def sysview_stop(self):
        self.monitor_run('esp sysview stop')

    def sysview_mcore_start(self, file):
        self.monitor_run('esp sysview_mcore start %s' % (file))


class OocdEsp32(OocdEspXtensa):
    """
        Class to communicate to OpenOCD supporting ESP32-specific features
    """
    chip_name = 'esp32'

    def __init__(self, oocd_exec=None, oocd_scripts=None, oocd_cfg_files=[], oocd_cfg_cmds=[],
                 oocd_debug=2, oocd_args=[], host='127.0.0.1', log_level=None, log_stream_handler=None, log_file_handler=None):
        super(OocdEsp32, self).__init__(cores_num=2, oocd_exec=oocd_exec, oocd_scripts=oocd_scripts,
                                         oocd_cfg_files=oocd_cfg_files, oocd_cfg_cmds=oocd_cfg_cmds, oocd_debug=oocd_debug,
                                         oocd_args=oocd_args, host=host, log_level=log_level, log_stream_handler=log_stream_handler,
                                         log_file_handler=log_file_handler)

class GdbEsp32(GdbEspXtensa):
    """
        Class to communicate to GDB supporting ESP32-specific features
    """
    chip_name = 'esp32'

    def __init__(self, gdb_path='xtensa-esp32-elf-gdb', remote_target=None, extended_remote_mode=False, gdb_log_file=None,
                 log_level=None, log_stream_handler=None, log_file_handler=None):
        super(GdbEsp32, self).__init__(gdb_path=gdb_path, remote_target=remote_target, extended_remote_mode=extended_remote_mode,
                                        gdb_log_file=gdb_log_file, log_level=log_level, log_stream_handler=log_stream_handler,
                                        log_file_handler=log_file_handler)


class OocdEsp32s2(OocdEspXtensa):
    """
        Class to communicate to OpenOCD supporting ESP32-specific features
    """
    chip_name = 'esp32s2'


class GdbEsp32s2(GdbEspXtensa):
    """
        Class to communicate to GDB supporting ESP32-specific features
    """
    chip_name = 'esp32s2'

    def __init__(self, gdb_path='xtensa-esp32s2-elf-gdb', remote_target=None, extended_remote_mode=False, gdb_log_file=None,
                 log_level=None, log_stream_handler=None, log_file_handler=None):
        super(GdbEsp32s2, self).__init__(gdb_path=gdb_path, remote_target=remote_target, extended_remote_mode=extended_remote_mode,
                                        gdb_log_file=gdb_log_file, log_level=log_level, log_stream_handler=log_stream_handler,
                                        log_file_handler=log_file_handler)
