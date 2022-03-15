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

from enum import IntEnum

# `typing` is used for provide Python2-compatible typing hint for IDEs like PyCharm.
# Some  other tools like flake8, language server of VSCode - Pylance  do not sopport it
# and can consider imports unused. To bypass the warning message `noqa` comment is used.
from typing import Tuple, Union  # noqa: F401
from . import debug_backend as dbg


class Modes(object):
    def __init__(self, modes_list=[]):
        for m in modes_list:
            setattr(self, m, m)

    @classmethod
    def get_dict(cls):
        public = {}
        for k, v in cls.__dict__.items():
            if k.startswith('_'):
                continue
            else:
                public[k] = v
        return public

    @classmethod
    def get_modes(cls):
        return list(cls.get_dict().values())


class DaOpenOcdModes(Modes):
    RUN_AND_CONNECT = 'run_and_connect'
    CONNECT = 'connect_to_instance'
    NO_OOCD = 'without_oocd'


class DaDevModes(Modes):
    NONE = "none"
    CON_CHECK = 'connection-check'
    X86 = 'x86-test'


class DaRunState(IntEnum):
    STOPPED = -2
    STOP_PREPARATION = -1
    UNKNOWN = 0
    RUNNING = 1
    READY_TO_CONNECT = 2
    CONNECTED = 3
    INITIALIZED = 4
    CONFIGURED = 5
    READY = 6


class DaVariableReference(IntEnum):
    LOCALS = 12
    REGISTERS = 24


class DaStates(object):
    general_state = DaRunState.STOPPED  # type: DaRunState
    ready = False  # TODO: replace to a lock
    no_debug = False  # argument of a launch request
    gdb_started = False
    ocd_started = False
    threads_updated = False  # True if something called a get_threads() method
    threads_are_stopped = None  # type: Union[bool, None]
    # sets to False after the update processed (for example, stopEvent generated)
    error = False
    start_time = None  # type: Union[str, None]
    wait_target_state = dbg.TARGET_STATE_UNKNOWN


class DaArgs(object):
    """
    Contains mandatory set of Da arguments. Can be extended with **kwargs
    """

    def __init__(self,
                 app_flash_off=None,
                 board_type="",
                 cmdfile="",
                 core_file=(),
                 debug=2,
                 developer_mode=None,
                 device_name="",
                 elfpath=(),
                 log_file=None,
                 log_mult_files=False,
                 log_no_debug_console=False,
                 oocd_args=None,
                 oocd_ip="",
                 oocd_mode="",
                 oocd_scripts="",
                 oocd="",
                 port=43474,
                 postmortem=False,
                 tmo_scale_factor=1,
                 toolchain_prefix="",
                 **kwargs):
        """

        Parameters
        ----------
        app_flash_off: Union[int, None]
        board_type: str
        cmdfile: str
        core_file: Tuple[str]
        debug: int
        developer_mode: Union[str, None]
        device_name: str
        elfpath: Tuple[str]
        log_file: str
        log_mult_files: bool
        log_no_debug_console:bool
        oocd: str
        oocd_args: str
        oocd_ip: str
        oocd_mode: str
        oocd_scripts: str
        port: int
        postmortem: bool
        tmo_scale_factor: int
        toolchain_prefix: str
        """
        self.app_flash_off = app_flash_off
        self.board_type = board_type
        self.debug = debug
        self.developer_mode = developer_mode
        self.device_name = device_name
        self.elfpath = elfpath
        self.cmdfile = cmdfile
        self.log_file = log_file
        self.log_mult_files = log_mult_files
        self.log_no_debug_console = log_no_debug_console
        self.oocd = oocd
        self.oocd_args = oocd_args
        self.oocd_ip = oocd_ip
        self.oocd_mode = oocd_mode
        self.oocd_scripts = oocd_scripts
        self.port = port
        self.toolchain_prefix = toolchain_prefix
        self.postmortem = postmortem
        self.core_file = core_file
        self.tmo_scale_factor = tmo_scale_factor
        # for key in kwargs:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_dict(self):
        return dict(self.__dict__)
