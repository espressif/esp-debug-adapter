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

from tests.conftest import setup_teardown, coredump_args, hostapp_args  # noqa: F401
from t_session import TSession
from tests import timeline
import pytest
# from tests.patterns import some
from tests.standard_requests import REQUEST_INIT, REQUEST_LAUNCH


@pytest.mark.timeout(30)
def test_init_launch_coredump(setup_teardown, coredump_args):  # noqa: F811
    with TSession(coredump_args) as ts:
        print("Session is run")
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)
        # if we have this event, GDB successfully loaded and started the application:
        expectation = timeline.Event("initialized")
        result = ts.wait_for(expectation, timeout_s=5)
        assert result
    print("Session is stopped")


@pytest.mark.timeout(30)
def test_init_launch_hostapp(setup_teardown, hostapp_args):  # noqa: F811
    with TSession(hostapp_args) as ts:
        print("Session is run")
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)
        # if we have this event, GDB successfully loaded and started the application:
        expectation = timeline.Event("initialized")
        result = ts.wait_for(expectation, timeout_s=5)
        assert result
    print("Session is stopped")


if __name__ == "__main__":
    # run tests from this file; print all output;
    pytest.main([__file__, "-s"])
