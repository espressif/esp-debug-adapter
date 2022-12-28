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
from re import match

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
    WATCH = 36


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


class Handle:
    START_HANDLE = 1000
    _next_handler = START_HANDLE + 1
    _handle_map = {}

    def __init__(self, start_handle: int) -> None:
        self._next_handler = start_handle if start_handle else self.START_HANDLE

    def create(self, val: list):
        self._next_handler = self._next_handler + 1
        self._handle_map[self._next_handler] = val
        return self._next_handler

    def get(self, ref):
        return self._handle_map[ref] if ref in self._handle_map and self._handle_map[ref] else None

    def get_handler(self):
        return self._next_handler

    def get_map(self):
        return self._handle_map

    def reset(self, start_handle: int):
        self._handle_map = {}
        self._next_handler = start_handle if start_handle else self.START_HANDLE


class VariableParser:
    result_regex = r'^([a-zA-Z_\-][a-zA-Z0-9_\-]*|\[\d+\])\s*=\s*'
    unknown_regex = r'\(.*?\)'
    variable_regex = r'^[a-zA-Z_\-][a-zA-Z0-9_\-]*'
    error_regex = r'^\<.+?\>'
    reference_string_regex = r'^(0x[0-9a-fA-F]+\s*)"'
    reference_regex = r'^0x[0-9a-fA-F]+'
    nullpointer_regex = r'^0x0+\\b'
    char_regex = r'^(\d+) [\'"]'
    number_regex = r'^\d+(\.\d+)?'
    pointer_combine_char_regex = '.'
    value_str = ''
    addr = 10000

    def __init__(self, value_str: str, addr: int = 10000) -> None:
        self.value_str = value_str
        self.handler = Handle(addr)
        self.handler.reset(addr)

    def parse_variable_value(self):
        self.value_str = self.value_str.strip()
        if self.value_str[0] == '{':
            result_dict = self.parse_tuple_dict()
            return result_dict
        elif self.value_str[0] == '"':
            return self.parse_cstring()
        else:
            return self.parse_primitive()

    def parse_tuple_dict(self):
        self.value_str = self.value_str.strip()
        if self.value_str[0] != '{':
            return None

        self.value_str = self.value_str[1:].strip()
        if self.value_str[0] == '}':
            self.value_str = self.value_str[1:].strip()
            return []
        if self.value_str.startswith('...'):
            self.value_str = self.value_str[3:].strip()
            if self.value_str[0] == '}':
                self.value_str = self.value_str[1:].strip()
                return '<...>'

        equalPos = self.value_str.find('=')
        newValPos1 = self.value_str.find('{')
        newValPos2 = self.value_str.find(',')
        newValPos = newValPos1
        if newValPos2 != -1 and newValPos2 < newValPos1:
            newValPos = newValPos2

        # Value list
        if ((newValPos != -1) and (equalPos > newValPos)) or equalPos == -1:
            return self.parse_tuple_dict_value_list()

        result = self.parse_result()
        if result:
            results = []
            results.append(result)
            comma_result = self.parse_comma_result()
            while comma_result:
                results.append(comma_result)
                comma_result = self.parse_comma_result()
            self.value_str = self.value_str[1:].strip()
            return results

    def parse_tuple_dict_value_list(self):
        result_values = []
        val = self.parse_variable_value()
        result_values.append(self.create_value('[0]', val))
        i = 0
        while True:
            i = i + 1
            val = self.parse_comma_value()
            if val is None:
                break
            result_values.append(
                self.create_value('[' + str(i) + ']', val))
        self.value_str = self.value_str[1:].strip()
        return result_values

    def parse_comma_result(self):
        self.value_str = self.value_str.strip()
        if self.value_str[0] != ',':
            return None
        self.value_str = self.value_str[1:].strip()
        # Remove comma values like \'\\000\' <repeats 25 times>,
        empty_comma_regex = r"\'\\\d+\'+.*?>,"
        var_match = match(empty_comma_regex, self.value_str)
        while var_match:
            self.value_str = self.value_str[len(var_match[0]):].strip()
            var_match = match(empty_comma_regex, self.value_str)
        return self.parse_result()

    def parse_comma_value(self):
        self.value_str = self.value_str.strip()
        if self.value_str[0] != ',':
            return None
        self.value_str = self.value_str[1:].strip()
        return self.parse_variable_value()

    def parse_cstring(self):
        self.value_str = self.value_str.strip()
        if self.value_str[0] != '"' and self.value_str[0] != '\'':
            return ''
        str_end = 1
        in_str = True
        char_str = self.value_str[0]
        remaining = self.value_str[1:]
        escaped = False
        while(in_str):
            if escaped:
                escaped = False
            elif remaining[0] == '\\':
                escaped = True
            elif remaining[0] == char_str:
                in_str = False
            remaining = remaining[1:]
            str_end = str_end + 1
        result_str = self.value_str[:str_end].strip()
        self.value_str = self.value_str[str_end:]
        return result_str

    def parse_primitive(self):
        self.value_str = self.value_str.strip()
        if len(self.value_str) == 0:
            return None
        elif self.value_str.startswith('true'):
            primitive = 'true'
            self.value_str = self.value_str[4:].strip()
        elif self.value_str.startswith('false'):
            primitive = 'false'
            self.value_str = self.value_str[5:].strip()
        else:
            primitive = self.parse_primitive_regex()

        if primitive is None:
            primitive = self.value_str

        return primitive

    def parse_primitive_regex(self):
        primitive = None
        regex_match = None
        for patt in (
            self.nullpointer_regex,
            self.reference_string_regex,
            self.reference_regex,
            self.char_regex,
            self.number_regex,
            self.variable_regex,
            self.unknown_regex,
            self.error_regex
        ):
            regex_match = match(patt, self.value_str)
            if regex_match:
                if patt == self.nullpointer_regex:
                    primitive = '<nullptr>'
                    self.value_str = self.value_str[len(
                        regex_match[0]):].strip()
                elif patt == self.reference_string_regex:
                    self.value_str = self.value_str[len(
                        regex_match[1]):].strip()
                    primitive = self.parse_cstring()
                elif patt == self.reference_regex:
                    primitive = '*' + regex_match[0]
                    self.value_str = self.value_str[len(
                        regex_match[0]):].strip()
                elif patt == self.char_regex:
                    primitive = regex_match[1]
                    self.value_str = self.value_str[len(
                        regex_match[0]) - 1:].strip()
                    primitive += ' ' + self.parse_cstring()
                elif patt == self.number_regex:
                    primitive = regex_match[0]
                    self.value_str = self.value_str[len(
                        regex_match[0]):].strip()
                elif patt == self.variable_regex or patt == self.error_regex or patt == self.unknown_regex:
                    primitive = regex_match[0]
                    self.value_str = self.value_str[len(regex_match[0]):].strip()
        return primitive

    def print_handles(self):
        print(self.get_variables())

    def get_variables(self):
        return self.handler.get_map()

    def parse_result(self):
        self.value_str = self.value_str.strip()
        var_match = match(self.result_regex, self.value_str)
        if var_match:
            self.value_str = self.value_str[len(var_match[0]):].strip()
            name = var_match[1]
            val = self.parse_variable_value()
            return self.create_value(name, val)

    def create_value(self, name: str, val):
        var_type = type(val)
        ref = 0
        return_val = val
        if var_type is list:
            ref = self.handler.create(val)
            return_val = '{...}'

        return {
            'name': name,
            'ref': ref,
            'value': return_val,
            'mem_addr': None
        }
