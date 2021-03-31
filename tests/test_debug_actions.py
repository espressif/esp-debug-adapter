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
from debug_adapter import schema
from t_session import TSession
import pytest
from tests.helpers import build_setbp_request, continue_till_stopped, get_top_frame_info, get_stack_trace
import timeline
from tests.standard_requests import REQUEST_INIT, REQUEST_LAUNCH
from tests.patterns import some
import time

@pytest.mark.timeout(30)
def test_threads(setup_teardown, coredump_args):  # noqa: F811
    with TSession(coredump_args) as ts:
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)
        rq = schema.Request(command="threads")
        resp = ts.send_request(rq)
        assert len(resp.body.get("threads")) == 4


@pytest.mark.timeout(30)
def test_stack(setup_teardown, coredump_args):  # noqa: F811
    with TSession(coredump_args) as ts:
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)
        rq = schema.Request(command="stackTrace",
                            arguments={
                                "format": {},
                                "levels": 20,
                                "startFrame": 0,
                                "threadId": 1
                            })
        resp = ts.send_request(rq)
        stack = resp.body.get("stackFrames")
        stack_sz = len(stack)
        assert stack[stack_sz - 1]["name"] == "app_main"


@pytest.mark.timeout(30)
def test_source_breakpoints(setup_teardown, hostapp_args):  # noqa: F811
    with TSession(hostapp_args) as ts:
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)
        rq = build_setbp_request("test_app.c", [{"line": 7}])
        resp = ts.send_request(rq)
        assert resp.success
        rq = build_setbp_request("test_app_src2.c", [{"line": 3}, {"line": 17}])
        resp = ts.send_request(rq)
        assert resp.success
        # run to the first breakpoint
        continue_till_stopped(ts, stop_reason="breakpoint", timeout=5)
        line, name = get_top_frame_info(ts, thread_id=1)
        assert name == "main"
        assert line == 7
        # run to  the next breakpoint
        continue_till_stopped(ts, stop_reason="breakpoint", timeout=5)
        line, name = get_top_frame_info(ts, thread_id=1)
        assert name == "print_hamlet"
        assert line == 3
        # run to  the next breakpoint
        continue_till_stopped(ts, stop_reason="breakpoint", timeout=5)
        line, name = get_top_frame_info(ts, thread_id=1)
        assert name == "print_hamlet"
        assert line == 17


@pytest.mark.timeout(30)
def test_continue(setup_teardown, hostapp_args):  # noqa: F811
    with TSession(hostapp_args) as ts:
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)

        rq = build_setbp_request("test_app.c", [{"line": 7}])
        resp = ts.send_request(rq)
        assert resp.success
        # run to the first breakpoint
        continue_till_stopped(ts, stop_reason="breakpoint", timeout=5)
        line, name = get_top_frame_info(ts, thread_id=1)
        assert name == "main"
        assert line == 7


@pytest.mark.timeout(30)
def test_pause(setup_teardown, hostapp_args):  # noqa: F811
    with TSession(hostapp_args) as ts:
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)

        rq = schema.ContinueRequest(arguments=schema.ContinueArguments(0))
        resp = ts.send_request(rq)
        assert resp.success

        time.sleep(3.0)
        rq = schema.PauseRequest(arguments=schema.PauseArguments(threadId=0))
        resp = ts.send_request(rq)
        assert resp.success

        expectation = timeline.Event(event="stopped", body=some.dict.containing({"reason": "pause"}))
        result = ts.wait_for(expectation, timeout_s=5)
        assert result


@pytest.mark.timeout(30)
def test_step(setup_teardown, hostapp_args):  # noqa: F811
    with TSession(hostapp_args) as ts:
        ts.send_request(REQUEST_INIT)
        ts.send_request(REQUEST_LAUNCH)

        # Set BP on `int lines = 0;` of `test_app.c`
        bpline = 4
        rq = build_setbp_request("test_app_src2.c", [{"line": bpline}])
        resp = ts.send_request(rq)
        assert resp.success
        # Continue to the BP
        continue_till_stopped(ts, stop_reason="breakpoint", timeout=5)
        line, name = get_top_frame_info(ts, thread_id=1)
        assert line == bpline
        assert name == "print_hamlet"

        # StepIn
        rq = schema.StepInRequest(schema.StepInArguments(threadId=1))
        resp = ts.send_request(rq)
        assert resp.success
        # Check the state
        line, name = get_top_frame_info(ts, thread_id=1)
        assert line == bpline + 1
        assert name == "print_hamlet"

        # StepOut
        rq = schema.StepOutRequest(schema.StepOutArguments(threadId=1))
        resp = ts.send_request(rq)
        assert resp.success
        # Check the state
        _, name = get_top_frame_info(ts, thread_id=1)
        assert name == "main"


if __name__ == "__main__":
    # run tests from this file; print all output;
    pytest.main([__file__, "-s"])
