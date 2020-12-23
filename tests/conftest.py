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

from tests import environment
from debug_adapter.internal_classes import DaOpenOcdModes
from datetime import datetime
import debug_adapter
import pytest
import os


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    see: https://docs.pytest.org/en/stable/reference.html#ini-options-ref
    """
    # set custom options only if none are provided from command line
    now = datetime.now()
    # create report target dir
    reports_dir = environment.ADAPTER_TOP_PATH / "tests" / "results"
    reports_dir.mkdir(parents=True, exist_ok=True)
    # custom report file
    config.option.xmlpath = str(reports_dir / ("report_%s.xml" % now.strftime('%H%M')))


@pytest.fixture()
def setup_teardown():
    print("setup")
    yield "setup_teardown"
    print("teardown")


@pytest.fixture
def coredump_args():
    da_args = debug_adapter.DaArgs()
    da_args.debug = 4
    da_args.elfpath = str(environment.ADAPTER_TOP_PATH / "tests" / "target" / "blink.elf")
    da_args.core_file = str(environment.ADAPTER_TOP_PATH / "tests" / "target" / "coredump.elf")
    da_args.port = 43474
    da_args.device_name = "esp32"
    da_args.postmortem = True
    da_args.log_file = "debug.log"
    da_args.log_no_debug_console = True
    return da_args


@pytest.fixture
def hostapp_args():
    da_args = debug_adapter.DaArgs()
    da_args.debug = 4
    testapp_name = "test_app"
    if os.name == 'nt':
        testapp_name += ".exe"
    da_args.elfpath = str(environment.ADAPTER_TOP_PATH / "tests" / "target" / "host" / testapp_name)
    da_args.log_file = "debug.log"
    da_args.log_no_debug_console = True
    da_args.oocd_mode = DaOpenOcdModes.NO_OOCD
    return da_args
