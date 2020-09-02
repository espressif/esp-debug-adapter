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
    STOPPED = -1
    UNKNOWN = 0
    CONNECTED = 1
    RUNNING = 2
    INITIALIZED = 3
    CONFIGURED = 4
    READY = 5


class DaStates(object):
    run_state = DaRunState.STOPPED  # type: DaRunState
    ready = False  # TODO: replace to a lock
    no_debug = False  # argument of a launch request
    gdb_started = False
    ocd_started = False
    wait_target_state = dbg.TARGET_STATE_UNKNOWN
    threads_updated = False  # True if something called a get_threads() method
    threads_are_stopped = None  # type: bool or None
    # sets to False after the update processed (for example, stopEvent generated)
    error = False
    start_time = None  # type: str


class DaArgs(object):
    """
    Contains mandatory set of Da arguments. Can be extended with **kwargs
    """

    def __init__(self, app_flash_off=None, board_type="", debug=2, device_name="",
                 developer_mode=None, postmortem=False, elfpath=(), log_file=None, log_mult_files=False, oocd="",
                 oocd_args=None, oocd_mode="", oocd_ip="", port=43474, oocd_scripts="", toolchain_prefix="",
                 cmdfile="", core_file=(), **kwargs):
        """

        Parameters
        ----------
        app_flash_off:int
        board_type:str
        debug:int
        developer_mode: str or None
        device_name:str
        elfpath:tuple
        log_file:str
        log_mult_files:bool
        oocd:str
        oocd_args:str
        oocd_ip:str
        oocd_mode:str
        oocd_scripts:str
        port:int
        toolchain_prefix:str
        cmdfile:str
        core_file: tuple
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
        self.oocd = oocd
        self.oocd_args = oocd_args
        self.oocd_ip = oocd_ip
        self.oocd_mode = oocd_mode
        self.oocd_scripts = oocd_scripts
        self.port = port
        self.toolchain_prefix = toolchain_prefix
        self.postmortem = postmortem
        self.core_file = core_file
        # for key in kwargs:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_dict(self):
        return dict(self.__dict__)
