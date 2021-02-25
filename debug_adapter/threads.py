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

import threading
import json
import itertools
from time import sleep
from . import base_schema, log
from .tools import PY3
from . import debug_backend as dbg

if PY3:
    _next_seq = itertools.count().__next__
else:
    _next_seq = itertools.count().next


class ReaderThread(threading.Thread):
    def __init__(self, stream, process_command):
        self.request_stop = False
        self._logger = log.new_logger("Debug Adapter (ReaderThread)", with_console_output=False)
        self.stream = stream  # stream to read
        self.process_command = process_command
        threading.Thread.__init__(self, name="ReaderThread")

    def run(self):
        data = None
        try:
            while not self.request_stop:
                try:
                    data = self.read()
                except RuntimeError as e:
                    self._logger.debug(e)
                if data is None:  # hence, EOF
                    break
                protocol_message = base_schema.from_dict(data)
                self.process_command(protocol_message)
        except Exception as e:
            if e == SystemExit:
                return
            log.debug_exception_no_con(e)

    def read(self):
        """
        Reads one message from the stream and returns the related dict (or None if EOF was reached).
        """
        headers = {}
        while True:
            # Interpret the http protocol headers
            try:
                line = self.stream.readline()  # The trailing \r\n should be there.
            except ConnectionResetError:
                self._logger.warning("Connection lost")
                break
            if not line:  # EOF
                self._logger.debug("EOF")
                return None
            self._logger.debug('read line: >>%s<<\n' % (line.replace(b'\r', b'\\r').replace(b'\n', b'\\n')), )
            line = line.strip().decode('ascii')
            if not line:  # Read just a new line without any contents
                break
            try:
                name, value = line.split(': ', 1)
            except ValueError:
                raise RuntimeError('invalid header line: {}'.format(line))
            headers[name] = value

        if not headers:
            raise RuntimeError('got message without headers')

        size = int(headers['Content-Length'])

        # Get the actual json
        body = self.stream.read(size)

        return json.loads(body.decode('utf-8'))

    def stop(self, blocking=True):
        self.request_stop = True
        if blocking:
            try:
                self.join()
            except RuntimeError:
                pass


class WriterThread(threading.Thread):
    def __init__(self, stream, queue):
        self.request_stop = False
        self._logger = log.new_logger("Debug Adapter (WriterThread)", with_console_output=False)
        self.stream = stream
        self.queue = queue
        threading.Thread.__init__(self, name="WriterThread")

    def run(self):
        try:
            while not self.request_stop:
                to_write = self.queue.get()
                to_json = getattr(to_write, 'to_json', None)
                if to_json is not None:
                    # Some protocol message
                    to_write.seq = _next_seq()
                    try:
                        to_write = to_json()
                    except Exception as e:
                        log.debug_exception_no_con(e)
                        log.debug_exception_no_con('Error serializing %s to json.' % (to_write, ))
                        continue

                self._logger.debug_no_con('Writing: %s\n' % (to_write, ))

                if to_write.__class__ == bytes:
                    as_bytes = to_write
                else:
                    as_bytes = to_write.encode('utf-8')

                self.stream.write(b'Content-Length: %d\r\n\r\n' % (len(as_bytes)))
                self.stream.write(as_bytes)
                self.stream.flush()
        except Exception as e:
            log.debug_exception_no_con(e)

    def stop(self, blocking=True):
        self.request_stop = True
        self.queue.put('exit')
        if blocking:
            try:
                self.join()
            except RuntimeError:
                pass


class TargetPollerThread(threading.Thread):
    def __init__(self, period, adapter_inst):
        self.period = period
        self.request_stop = False
        self._logger = log.new_logger("Debug Adapter (TargetPollerThread)", with_console_output=False)
        self.adapter = adapter_inst
        threading.Thread.__init__(self, name="TargetPollerThread")

    def run(self, wait_target_state):
        try:
            self._logger.debug("Start. Waiting for target state: %d", wait_target_state)
            self.wait_target_state = wait_target_state
            while not self.request_stop:
                if self.wait_target_state == dbg.TARGET_STATE_STOPPED:
                    stopped, rsn_str = self.adapter.is_stopped()
                    if stopped:
                        self.stop(blocking=False)
                        self.adapter._cmd_exec.generate_StoppedEvent(reason=rsn_str,
                                                                     thread_id=0,
                                                                     all_threads_stopped=True)
                elif self.wait_target_state == dbg.TARGET_STATE_RUNNING:
                    # this is not fully implemented yet, need to define when we need to start waiting for
                    # target get running
                    try:
                        self.adapter._gdb.wait_target_state(dbg.TARGET_STATE_RUNNING, 0)
                        self.wait_target_state = dbg.TARGET_STATE_UNKNOWN
                        self.adapter._cmd_exec.generate_ContinuedEvent(thread_id=0, all_threads_continued=True)
                    except dbg.DebuggerTargetStateTimeoutError:
                        pass
                else:
                    pass
                sleep(self.period)
        except Exception as e:
            log.debug_exception_no_con(e)

    def stop(self, blocking=True):
        self.request_stop = True
        self.wait_target_state = dbg.TARGET_STATE_UNKNOWN
        if blocking:
            try:
                self.join()
            except RuntimeError:
                pass
