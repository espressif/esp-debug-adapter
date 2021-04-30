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

import pathlib
from debug_adapter import schema
import timeline
from tests.patterns import some


def build_setbp_request(path, bps):
    if isinstance(path, pathlib.Path):
        path = str(path)
    rq = schema.SetBreakpointsRequest(arguments={
        "source": schema.Source(path=path),
        "breakpoints": bps,
    })
    return rq


def set_breakpoints(ts, path, bps):
    rq = build_setbp_request(path, bps)
    resp = ts.send_request(rq)
    assert resp.success


def continue_till_stopped(ts, stop_reason, thread_id=None, timeout=5):
    rq = schema.ContinueRequest(arguments=schema.ContinueArguments(0))
    resp = ts.send_request(rq)
    assert resp.success

    expect_body = {"reason": stop_reason}
    if thread_id is not None:
        expect_body['threadId'] = thread_id
    expectation = timeline.Event(event="stopped", body=some.dict.containing(expect_body))
    result = ts.wait_for(expectation, timeout_s=timeout)
    assert result


def get_stack_trace(ts, thread_id, start, num):
    rq = schema.StackTraceRequest(arguments=schema.StackTraceArguments(threadId=thread_id, startFrame=0, levels=20))
    resp = ts.send_request(rq)
    return resp.body.get("stackFrames")


def get_top_frame_info(ts, thread_id):
    stack = get_stack_trace(ts, thread_id, 0, 1)
    assert len(stack) > 0
    line = stack[0].get("line")
    name = stack[0].get("name")
    return line, name
