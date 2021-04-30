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

from debug_adapter import DebugAdapter, schema, log
from debug_adapter.internal_classes import DaArgs, DaRunState
from debugpy.common import messaging
from debugpy.common.messaging import JsonIOStream
from debugpy.common.sockets import create_client
from tests import timeline
from threading import Thread, Lock
from typing import Union
import collections
import functools
import itertools
import json
import select
import socket
import time


class MessageFactory(object):
    """A factory for DAP messages that are not bound to a message channel.
    """
    def __init__(self):
        self._seq_iter = itertools.count(1)
        self.messages = collections.OrderedDict()
        self.event = functools.partial(self._make, messaging.Event)
        self.request = functools.partial(self._make, messaging.Request)
        self.response = functools.partial(self._make, messaging.Response)

    def _make(self, message_type, *args, **kwargs):
        message = message_type(None, next(self._seq_iter), *args, **kwargs)
        self.messages[message.seq] = message
        return message


class TSession:
    def __init__(self, adapter_args, name="noname"):
        """
        Test session.

        Parameters
        ----------
        adapter_args : DaArgs
            [description]
        """
        self.session_name = name  # type: str
        self._adapter_args = adapter_args  # type: DaArgs
        self._adapter_obj = None  # type: Union[DebugAdapter, None]
        self._adapter_thread = None  # type: Union[Thread, None]
        # self._client = None  # type: ClientDa
        self._client_stream = None  # type: Union[JsonIOStream, None]
        self._client_socket = None  # type: Union[socket.socket, None]
        self.session_timeline = timeline.Timeline("Timeline of \"%s\"" % self.session_name)
        self._message_factory = MessageFactory()
        self._reader_thread = None  # type: Union[Thread, None]
        self._ongoing_request = None  # used for catching responses. Will set to None after every recorded responce
        self._last_response = None
        self.__stop = False
        self.client_busy = Lock()

    def __enter__(self):
        log.info("================ Debug session ENTER: %s ================ " % self.session_name)
        self.session_start()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if self.session_timeline.is_frozen:
            self.session_timeline.unfreeze()

        if exception_type is not None:
            print("closed with exception: " + str(exception_type))
        self.session_stop()

        # Inherited from debugpy -----------------------------------------------
        # # Work around https://bugs.python.org/issue37380
        # for popen in self.debuggee, self.adapter:
        #     if popen is not None and popen.returncode is None:
        #         popen.returncode = -1

    def is_input_message(self, timeout_s):
        ready, _, _ = select.select([self._client_socket], [], [], timeout_s)
        if len(ready):
            return True
        return False

    def session_start(self):
        self.start_adapter()
        while not self._adapter_obj.state.general_state == DaRunState.READY_TO_CONNECT:
            pass
        self.start_client()
        self._reader_thread = Thread(target=self._client_stream_monitor)
        self._reader_thread.start()

    def session_stop(self):
        self.__stop = True
        while self.client_busy.locked():
            pass  # waiting for finishing of operations
        if self._adapter_obj:
            disconnect_rq = schema.Request(command="disconnect", seq=-1, arguments={"restart": False})
            self.send_request(disconnect_rq, False)
            # give adapter time to cleanup
            time.sleep(2.0)
        if self._client_stream and not self._client_stream._closed:
            self._client_stream.close()
        if self._client_socket and not self._client_socket._closed:
            self._client_socket.close()
        # avoid errors due to unobserved responses and events
        # TODO: avoid using 'TSession.wait_for' in tests. Instead of it,
        # compose expected message sequences and use 'timeline.wait_until_realized'.
        # Using that approach we will ensure that communication is done as expected and
        # do not need to call `timeline.observe_all`
        with self.session_timeline.frozen():
            self.session_timeline.observe_all()
        self.session_timeline.close()

    def start_client(self):
        self._client_socket = create_client()
        self._client_socket.connect(("127.0.0.1", self._adapter_args.port))
        self._client_stream = JsonIOStream.from_socket(self._client_socket)

    def start_adapter(self):
        self._adapter_obj = DebugAdapter(self._adapter_args)
        self._adapter_thread = Thread(target=self._adapter_obj.adapter_run)
        self._adapter_thread.start()

    def send_request(self, request: Union[schema.Request, dict], wait_responce=True):
        """
        Parameters
        ----------
        request : Union[schema.Request, dict]
        """
        if isinstance(request, dict):
            request_dict = request
        else:
            request_dict = request.to_dict()
        self._client_stream.write_json(request_dict)
        request_msg = self._message_factory.request(request.command, request.arguments)
        self._ongoing_request = self.session_timeline.record_request(request_msg)

        log.warning("--->>> SENT JSON: %s" % request_dict)
        if wait_responce:
            while self._ongoing_request:
                pass
            assert request.command == self._last_response.command
            # TODO: Enable check below, currently DebugAdapter does not reflect request_seq in responses
            # assert self._ongoing_request.message.seq == self._last_response.request_seq
        return self._last_response

    def is_in_timeline(self, expectation):
        with self.session_timeline.frozen():
            return expectation in self.session_timeline

    def wait_for(self, expectation, timeout_s=0):
        if timeout_s is not None:
            end = time.process_time() + timeout_s
        while not self.is_in_timeline(expectation):
            if timeout_s is not None and (time.process_time() >= end):
                return False
        return True

    def _client_stream_monitor(self):
        while not self.__stop:
            try:
                with self.client_busy:
                    if self.is_input_message(0.05):
                        new_json = self._client_stream.read_json()
                        log.warning("<<<---  NEW JSON: %s" % new_json)
                        new_json_type = new_json.get("type")
                        if new_json_type == "event":
                            event_msg = self._message_factory.event(new_json["event"], new_json.get("body", {}))
                            event_msg.seq = new_json["seq"]
                            self.session_timeline.record_event(event_msg)
                        elif new_json_type == "response":
                            assert self._ongoing_request
                            response_msg = self._message_factory.response(new_json["command"], new_json.get("body", {}))
                            response_msg.seq = new_json["request_seq"]
                            response_msg.request = self._ongoing_request.message
                            self._last_response = schema.Response(
                                seq=response_msg.seq,
                                request_seq=self._ongoing_request.seq,
                                success=response_msg.success,
                                body=response_msg.body,
                                command=response_msg.request.command
                            )
                            self.session_timeline.record_response(self._ongoing_request, response_msg)
                            self._ongoing_request = None
                        else:
                            log.warning("Unknown message: %s" % new_json)
                    else:
                        pass
            except json.decoder.JSONDecodeError as e:
                log.warning("Failed to decode JSON: %s!" % e)
            except messaging.NoMoreMessages:
                pass
