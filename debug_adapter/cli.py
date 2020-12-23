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

import os
import sys
import click
from typing import Union
from .debug_adapter import A2VSC_STARTED_STRING, DebugAdapter
from .internal_classes import DaDevModes, DaOpenOcdModes, DaArgs

h = {
    "--app_flash_off": 'Program start address offset (ESP32_APP_FLASH_OFF). The value can be in decimal, binary, octal \
        or hexadecimal formats',
    "--board-type": 'Type of the board to run tests on (you could use OOCD_TEST_BOARD envvar by default)',
    "--debug": 'Debug level (0-4), 5 - for a full OOCD log',
    "--developer-mode": 'Modes for development purposes',
    "--device-name": 'The name of used hardware to debug (currently Esp32 or Esp32_S2). It defines '
    '--toolchain-prefix',
    "--port": "Listen on given port for VS Code connections",
    "--log-file": 'Path to log file.',
    "--log-mult-files": 'Log to separated files',
    "--log-no-debug-console": 'Turn off output to the debug console of the IDE',
    "--toolchain-prefix": '(If not set, controlled by --device-name!) Toolchain prefix. If set, rewrites the value '
    'specified by --device-name.',
    "--elfpath": 'A path to elf files for debugging. You can use several elf files e.g. `-e file1.elf -e '
    'file2.elf`',
    "--core-file": 'Use a file as a core dump to examine.',
    "--oocd": 'Path to OpenOCD binary file, (used OPENOCD_BIN envvar or (if not set) '
    '\'openocd\' by default)',
    "--oocd-args": "(If not set, drives by --device-name!) Specifies custom OpenOCD args. If set, rewrites the"
    " value specified by --device-name.",
    "--oocd-mode": 'Cooperation with OpenOCD',
    "--oocd-ip": "Ip for remote OpenOCD connection",
    "--postmortem": "Run the adapter without target in \'read-only\' mode",
    "--oocd-scripts": 'Path to OpenOCD TCL scripts (use OPENOCD_SCRIPTS envvar by default)',
    "--cmdfile": 'Path to a command file containing commands to automatic execute during a program startup',
}


class IntegerWithPrefix(click.ParamType):
    """
    Custom Cick type accepting numbers in different basis
    """
    name = 'integer_with_prefix'

    def convert(self, value, param, ctx):
        try:
            if isinstance(value, int):
                return value
            if (isinstance(value, str) and len(value) > 1 and value[0] == '0' and value[1].isnumeric()):
                # convert 0123 as 8-based 123
                return int(value, 8)
            return int(value, 0)
        except ValueError:
            self.fail('%s is not a valid integer' % value, param, ctx)


INT_PREF = IntegerWithPrefix()


# TODO Toolchain from "idf.xtensaEsp32Path" settings.json
# TODO xtensaEsp32Path -> xtensaEspToolchainPath, espToolchainPath
@click.command()
# Basic parameters:
@click.option("--app_flash_off", "-a", help=h["--app_flash_off"], type=INT_PREF, default=0x10000, show_default=True)
@click.option('--board-type', '-b', help=h['--board-type'], type=Union[str])
@click.option('--debug', '-d', help=h['--debug'], type=INT_PREF, default=2, show_default=True)
@click.option('--device-name', '-dn', help=h['--device-name'], type=Union[str], default=None, show_default=True)
@click.option('--port', '-p', help=h['--port'], default=43474, show_default=True, type=INT_PREF)
#
# Specific modes:
@click.option('--postmortem', '-pm', help=h['--postmortem'], is_flag=True)
@click.option('--developer-mode',
              help=h['--developer-mode'],
              type=click.Choice(DaDevModes.get_modes()),
              default=DaDevModes.NONE,
              show_default=True)
# logging parameters:
@click.option('--log-file', '-l', help=h['--log-file'], type=Union[str])
@click.option('--log-mult-files', '-lm', help=h['--log-mult-files'], default=None, is_flag=True)
@click.option('--log-no-debug-console', '-ln', help=h['--log-no-debug-console'], default=None, is_flag=True)
#
# GDB parameters:
@click.option('--toolchain-prefix',
              '-t',
              help=h['--toolchain-prefix'],
              type=Union[str],
              default=None,
              show_default=True)
@click.option('--elfpath', '-e', help=h['--elfpath'], multiple=True, default=None, type=Union[str])
@click.option('--core-file', '-c', help=h['--core-file'], multiple=True, default=None, type=Union[str])
@click.option('--cmdfile', '-x', help=h['--cmdfile'], default=None, type=Union[str])
#
# OpenOCD parameters:
@click.option('--oocd', '-o', help=h['--oocd'], default=os.environ.get("OPENOCD_BIN", "openocd"), show_default=True)
@click.option('--oocd-args', '-oa', help=h['--oocd-args'], default=None, show_default=True)
@click.option('--oocd-mode',
              '-om',
              help=h['--oocd-mode'],
              type=click.Choice(DaOpenOcdModes.get_modes()),
              default=DaOpenOcdModes.CONNECT,
              show_default=True)
@click.option('--oocd-ip', '-ip', help=h['--oocd-ip'], default='localhost', show_default=True, type=Union[str])
@click.option('--oocd-scripts', '-s', help=h['--oocd-scripts'], default=None, show_default=True)
#
@click.pass_context
def cli(ctx, **kwargs):
    args_main = DaArgs(**ctx.params)
    # Modificators
    if args_main.developer_mode == DaDevModes.X86:
        args_main.debug = 5
        args_main.log_file = "debug.log"
        args_main.oocd_mode = DaOpenOcdModes.NO_OOCD
        args_main.toolchain_prefix = ""
        args_main.elfpath = ""

    if args_main.developer_mode == DaDevModes.CON_CHECK:
        args_main.debug = 4
        args_main.port = 43474
        args_main.oocd_mode = DaOpenOcdModes.NO_OOCD
        args_main.log_file = "debug.log"
    # Real work starts here
    dbg_a = DebugAdapter(args=args_main)
    dbg_a.log_cmd(A2VSC_STARTED_STRING)
    dbg_a.adapter_run()


if __name__ == '__main__':
    cli(sys.argv[1:])
