# -*- coding: utf-8 -*-
# Note: automatically generated code. Do not edit manually.
from .base_schema import BaseSchema, register, register_request, register_response


@register
class ProtocolMessage(BaseSchema):
    """
    Base class of requests, responses, and events.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "description": "Message type.",
            "_enum": [
                "request",
                "response",
                "event"
            ]
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, type, seq=-1, **kwargs):
        """
        :param string type: Message type.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = type
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class Request(BaseSchema):
    """
    A client or debug adapter initiated request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "description": "The command to execute."
        },
        "arguments": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Object containing arguments for the command."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, command, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: The command to execute.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] arguments: Object containing arguments for the command.
        """
        self.type = 'request'
        self.command = command
        self.seq = seq
        self.arguments = arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments
        dct.update(self.kwargs)
        return dct


@register
class Event(BaseSchema):
    """
    A debug adapter initiated event.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "description": "Type of event."
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Event-specific information."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, event, seq=-1, body=None, **kwargs):
        """
        :param string type: 
        :param string event: Type of event.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Event-specific information.
        """
        self.type = 'event'
        self.event = event
        self.seq = seq
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'seq': self.seq,
        }
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register
class Response(BaseSchema):
    """
    Response for a request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_response('error')
@register
class ErrorResponse(BaseSchema):
    """
    On error (whenever 'success' is false), the body can provide more details.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "error": {
                    "$ref": "#/definitions/Message",
                    "description": "An optional, structured error message."
                }
            }
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param ErrorResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = ErrorResponseBody()
        else:
            self.body = ErrorResponseBody(**body) if body.__class__ !=  ErrorResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('cancel')
@register
class CancelRequest(BaseSchema):
    """
    The 'cancel' request is used by the frontend in two situations:
    
    - to indicate that it is no longer interested in the result produced by a specific request issued
    earlier
    
    - to cancel a progress sequence. Clients should only call this request if the capability
    'supportsCancelRequest' is true.
    
    This request has a hint characteristic: a debug adapter can only be expected to make a 'best effort'
    in honouring this request but there are no guarantees.
    
    The 'cancel' request may return an error if it could not cancel an operation but a frontend should
    refrain from presenting this error to end users.
    
    A frontend client should only call this request if the capability 'supportsCancelRequest' is true.
    
    The request that got canceled still needs to send a response back. This can either be a normal
    result ('success' attribute true)
    
    or an error response ('success' attribute false and the 'message' set to 'cancelled').
    
    Returning partial results from a cancelled request is possible but please note that a frontend
    client has no generic way for detecting that a response is partial or not.
    
    The progress that got cancelled still needs to send a 'progressEnd' event back.
    
    A client should not assume that progress just got cancelled after sending the 'cancel' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "cancel"
            ]
        },
        "arguments": {
            "type": "CancelArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param CancelArguments arguments: 
        """
        self.type = 'request'
        self.command = 'cancel'
        self.seq = seq
        if arguments is None:
            self.arguments = CancelArguments()
        else:
            self.arguments = CancelArguments(**arguments) if arguments.__class__ !=  CancelArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class CancelArguments(BaseSchema):
    """
    Arguments for 'cancel' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "requestId": {
            "type": "integer",
            "description": "The ID (attribute 'seq') of the request to cancel. If missing no request is cancelled.\nBoth a 'requestId' and a 'progressId' can be specified in one request."
        },
        "progressId": {
            "type": "string",
            "description": "The ID (attribute 'progressId') of the progress to cancel. If missing no progress is cancelled.\nBoth a 'requestId' and a 'progressId' can be specified in one request."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, requestId=None, progressId=None, **kwargs):
        """
        :param integer requestId: The ID (attribute 'seq') of the request to cancel. If missing no request is cancelled.
        Both a 'requestId' and a 'progressId' can be specified in one request.
        :param string progressId: The ID (attribute 'progressId') of the progress to cancel. If missing no progress is cancelled.
        Both a 'requestId' and a 'progressId' can be specified in one request.
        """
        self.requestId = requestId
        self.progressId = progressId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.requestId is not None:
            dct['requestId'] = self.requestId
        if self.progressId is not None:
            dct['progressId'] = self.progressId
        dct.update(self.kwargs)
        return dct


@register_response('cancel')
@register
class CancelResponse(BaseSchema):
    """
    Response to 'cancel' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register
class InitializedEvent(BaseSchema):
    """
    This event indicates that the debug adapter is ready to accept configuration requests (e.g.
    SetBreakpointsRequest, SetExceptionBreakpointsRequest).
    
    A debug adapter is expected to send this event when it is ready to accept configuration requests
    (but not before the 'initialize' request has finished).
    
    The sequence of events/requests is as follows:
    
    - adapters sends 'initialized' event (after the 'initialize' request has returned)
    
    - frontend sends zero or more 'setBreakpoints' requests
    
    - frontend sends one 'setFunctionBreakpoints' request (if capability 'supportsFunctionBreakpoints'
    is true)
    
    - frontend sends a 'setExceptionBreakpoints' request if one or more 'exceptionBreakpointFilters'
    have been defined (or if 'supportsConfigurationDoneRequest' is not defined or false)
    
    - frontend sends other future configuration requests
    
    - frontend sends one 'configurationDone' request to indicate the end of the configuration.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "initialized"
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Event-specific information."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, body=None, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Event-specific information.
        """
        self.type = 'event'
        self.event = 'initialized'
        self.seq = seq
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'seq': self.seq,
        }
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register
class StoppedEvent(BaseSchema):
    """
    The event indicates that the execution of the debuggee has stopped due to some condition.
    
    This can be caused by a break point previously set, a stepping request has completed, by executing a
    debugger statement etc.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "stopped"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason for the event.\nFor backward compatibility this string is shown in the UI if the 'description' attribute is missing (but it must not be translated).",
                    "_enum": [
                        "step",
                        "breakpoint",
                        "exception",
                        "pause",
                        "entry",
                        "goto",
                        "function breakpoint",
                        "data breakpoint",
                        "instruction breakpoint"
                    ]
                },
                "description": {
                    "type": "string",
                    "description": "The full reason for the event, e.g. 'Paused on exception'. This string is shown in the UI as is and must be translated."
                },
                "threadId": {
                    "type": "integer",
                    "description": "The thread which was stopped."
                },
                "preserveFocusHint": {
                    "type": "boolean",
                    "description": "A value of true hints to the frontend that this event should not change the focus."
                },
                "text": {
                    "type": "string",
                    "description": "Additional information. E.g. if reason is 'exception', text contains the exception name. This string is shown in the UI."
                },
                "allThreadsStopped": {
                    "type": "boolean",
                    "description": "If 'allThreadsStopped' is true, a debug adapter can announce that all threads have stopped.\n- The client should use this information to enable that all threads can be expanded to access their stacktraces.\n- If the attribute is missing or false, only the thread with the given threadId can be expanded."
                }
            },
            "required": [
                "reason"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param StoppedEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'stopped'
        if body is None:
            self.body = StoppedEventBody()
        else:
            self.body = StoppedEventBody(**body) if body.__class__ !=  StoppedEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ContinuedEvent(BaseSchema):
    """
    The event indicates that the execution of the debuggee has continued.
    
    Please note: a debug adapter is not expected to send this event in response to a request that
    implies that execution continues, e.g. 'launch' or 'continue'.
    
    It is only necessary to send a 'continued' event if there was no previous request that implied this.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "continued"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "threadId": {
                    "type": "integer",
                    "description": "The thread which was continued."
                },
                "allThreadsContinued": {
                    "type": "boolean",
                    "description": "If 'allThreadsContinued' is true, a debug adapter can announce that all threads have continued."
                }
            },
            "required": [
                "threadId"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ContinuedEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'continued'
        if body is None:
            self.body = ContinuedEventBody()
        else:
            self.body = ContinuedEventBody(**body) if body.__class__ !=  ContinuedEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ExitedEvent(BaseSchema):
    """
    The event indicates that the debuggee has exited and returns its exit code.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "exited"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "exitCode": {
                    "type": "integer",
                    "description": "The exit code returned from the debuggee."
                }
            },
            "required": [
                "exitCode"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ExitedEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'exited'
        if body is None:
            self.body = ExitedEventBody()
        else:
            self.body = ExitedEventBody(**body) if body.__class__ !=  ExitedEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class TerminatedEvent(BaseSchema):
    """
    The event indicates that debugging of the debuggee has terminated. This does **not** mean that the
    debuggee itself has exited.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "terminated"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "restart": {
                    "type": [
                        "array",
                        "boolean",
                        "integer",
                        "null",
                        "number",
                        "object",
                        "string"
                    ],
                    "description": "A debug adapter may set 'restart' to true (or to an arbitrary object) to request that the front end restarts the session.\nThe value is not interpreted by the client and passed unmodified as an attribute '__restart' to the 'launch' and 'attach' requests."
                }
            }
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, body=None, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param TerminatedEventBody body: 
        """
        self.type = 'event'
        self.event = 'terminated'
        self.seq = seq
        if body is None:
            self.body = TerminatedEventBody()
        else:
            self.body = TerminatedEventBody(**body) if body.__class__ !=  TerminatedEventBody else body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'seq': self.seq,
        }
        if self.body is not None:
            dct['body'] = self.body.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class ThreadEvent(BaseSchema):
    """
    The event indicates that a thread has started or exited.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "thread"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason for the event.",
                    "_enum": [
                        "started",
                        "exited"
                    ]
                },
                "threadId": {
                    "type": "integer",
                    "description": "The identifier of the thread."
                }
            },
            "required": [
                "reason",
                "threadId"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ThreadEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'thread'
        if body is None:
            self.body = ThreadEventBody()
        else:
            self.body = ThreadEventBody(**body) if body.__class__ !=  ThreadEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class OutputEvent(BaseSchema):
    """
    The event indicates that the target has produced some output.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "output"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The output category. If not specified, 'console' is assumed.",
                    "_enum": [
                        "console",
                        "stdout",
                        "stderr",
                        "telemetry"
                    ]
                },
                "output": {
                    "type": "string",
                    "description": "The output to report."
                },
                "group": {
                    "type": "string",
                    "description": "Support for keeping an output log organized by grouping related messages.",
                    "enum": [
                        "start",
                        "startCollapsed",
                        "end"
                    ],
                    "enumDescriptions": [
                        "Start a new group in expanded mode. Subsequent output events are members of the group and should be shown indented.\nThe 'output' attribute becomes the name of the group and is not indented.",
                        "Start a new group in collapsed mode. Subsequent output events are members of the group and should be shown indented (as soon as the group is expanded).\nThe 'output' attribute becomes the name of the group and is not indented.",
                        "End the current group and decreases the indentation of subsequent output events.\nA non empty 'output' attribute is shown as the unindented end of the group."
                    ]
                },
                "variablesReference": {
                    "type": "integer",
                    "description": "If an attribute 'variablesReference' exists and its value is > 0, the output contains objects which can be retrieved by passing 'variablesReference' to the 'variables' request. The value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "source": {
                    "$ref": "#/definitions/Source",
                    "description": "An optional source location where the output was produced."
                },
                "line": {
                    "type": "integer",
                    "description": "An optional source location line where the output was produced."
                },
                "column": {
                    "type": "integer",
                    "description": "An optional source location column where the output was produced."
                },
                "data": {
                    "type": [
                        "array",
                        "boolean",
                        "integer",
                        "null",
                        "number",
                        "object",
                        "string"
                    ],
                    "description": "Optional data to report. For the 'telemetry' category the data will be sent to telemetry, for the other categories the data is shown in JSON format."
                }
            },
            "required": [
                "output"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param OutputEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'output'
        if body is None:
            self.body = OutputEventBody()
        else:
            self.body = OutputEventBody(**body) if body.__class__ !=  OutputEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class BreakpointEvent(BaseSchema):
    """
    The event indicates that some information about a breakpoint has changed.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "breakpoint"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason for the event.",
                    "_enum": [
                        "changed",
                        "new",
                        "removed"
                    ]
                },
                "breakpoint": {
                    "$ref": "#/definitions/Breakpoint",
                    "description": "The 'id' attribute is used to find the target breakpoint and the other attributes are used as the new values."
                }
            },
            "required": [
                "reason",
                "breakpoint"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param BreakpointEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'breakpoint'
        if body is None:
            self.body = BreakpointEventBody()
        else:
            self.body = BreakpointEventBody(**body) if body.__class__ !=  BreakpointEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ModuleEvent(BaseSchema):
    """
    The event indicates that some information about a module has changed.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "module"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason for the event.",
                    "enum": [
                        "new",
                        "changed",
                        "removed"
                    ]
                },
                "module": {
                    "$ref": "#/definitions/Module",
                    "description": "The new, changed, or removed module. In case of 'removed' only the module id is used."
                }
            },
            "required": [
                "reason",
                "module"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ModuleEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'module'
        if body is None:
            self.body = ModuleEventBody()
        else:
            self.body = ModuleEventBody(**body) if body.__class__ !=  ModuleEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class LoadedSourceEvent(BaseSchema):
    """
    The event indicates that some source has been added, changed, or removed from the set of all loaded
    sources.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "loadedSource"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason for the event.",
                    "enum": [
                        "new",
                        "changed",
                        "removed"
                    ]
                },
                "source": {
                    "$ref": "#/definitions/Source",
                    "description": "The new, changed, or removed source."
                }
            },
            "required": [
                "reason",
                "source"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param LoadedSourceEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'loadedSource'
        if body is None:
            self.body = LoadedSourceEventBody()
        else:
            self.body = LoadedSourceEventBody(**body) if body.__class__ !=  LoadedSourceEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ProcessEvent(BaseSchema):
    """
    The event indicates that the debugger has begun debugging a new process. Either one that it has
    launched, or one that it has attached to.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "process"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The logical name of the process. This is usually the full path to process's executable file. Example: /home/example/myproj/program.js."
                },
                "systemProcessId": {
                    "type": "integer",
                    "description": "The system process id of the debugged process. This property will be missing for non-system processes."
                },
                "isLocalProcess": {
                    "type": "boolean",
                    "description": "If true, the process is running on the same computer as the debug adapter."
                },
                "startMethod": {
                    "type": "string",
                    "enum": [
                        "launch",
                        "attach",
                        "attachForSuspendedLaunch"
                    ],
                    "description": "Describes how the debug engine started debugging this process.",
                    "enumDescriptions": [
                        "Process was launched under the debugger.",
                        "Debugger attached to an existing process.",
                        "A project launcher component has launched a new process in a suspended state and then asked the debugger to attach."
                    ]
                },
                "pointerSize": {
                    "type": "integer",
                    "description": "The size of a pointer or address for this process, in bits. This value may be used by clients when formatting addresses for display."
                }
            },
            "required": [
                "name"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ProcessEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'process'
        if body is None:
            self.body = ProcessEventBody()
        else:
            self.body = ProcessEventBody(**body) if body.__class__ !=  ProcessEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class CapabilitiesEvent(BaseSchema):
    """
    The event indicates that one or more capabilities have changed.
    
    Since the capabilities are dependent on the frontend and its UI, it might not be possible to change
    that at random times (or too late).
    
    Consequently this event has a hint characteristic: a frontend can only be expected to make a 'best
    effort' in honouring individual capabilities but there are no guarantees.
    
    Only changed capabilities need to be included, all other capabilities keep their values.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "capabilities"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "capabilities": {
                    "$ref": "#/definitions/Capabilities",
                    "description": "The set of updated capabilities."
                }
            },
            "required": [
                "capabilities"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param CapabilitiesEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'capabilities'
        if body is None:
            self.body = CapabilitiesEventBody()
        else:
            self.body = CapabilitiesEventBody(**body) if body.__class__ !=  CapabilitiesEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ProgressStartEvent(BaseSchema):
    """
    The event signals that a long running operation is about to start and
    
    provides additional information for the client to set up a corresponding progress and cancellation
    UI.
    
    The client is free to delay the showing of the UI in order to reduce flicker.
    
    This event should only be sent if the client has passed the value true for the
    'supportsProgressReporting' capability of the 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "progressStart"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "progressId": {
                    "type": "string",
                    "description": "An ID that must be used in subsequent 'progressUpdate' and 'progressEnd' events to make them refer to the same progress reporting.\nIDs must be unique within a debug session."
                },
                "title": {
                    "type": "string",
                    "description": "Mandatory (short) title of the progress reporting. Shown in the UI to describe the long running operation."
                },
                "requestId": {
                    "type": "number",
                    "description": "The request ID that this progress report is related to. If specified a debug adapter is expected to emit\nprogress events for the long running request until the request has been either completed or cancelled.\nIf the request ID is omitted, the progress report is assumed to be related to some general activity of the debug adapter."
                },
                "cancellable": {
                    "type": "boolean",
                    "description": "If true, the request that reports progress may be canceled with a 'cancel' request.\nSo this property basically controls whether the client should use UX that supports cancellation.\nClients that don't support cancellation are allowed to ignore the setting."
                },
                "message": {
                    "type": "string",
                    "description": "Optional, more detailed progress message."
                },
                "percentage": {
                    "type": "number",
                    "description": "Optional progress percentage to display (value range: 0 to 100). If omitted no percentage will be shown."
                }
            },
            "required": [
                "progressId",
                "title"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ProgressStartEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'progressStart'
        if body is None:
            self.body = ProgressStartEventBody()
        else:
            self.body = ProgressStartEventBody(**body) if body.__class__ !=  ProgressStartEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ProgressUpdateEvent(BaseSchema):
    """
    The event signals that the progress reporting needs to updated with a new message and/or percentage.
    
    The client does not have to update the UI immediately, but the clients needs to keep track of the
    message and/or percentage values.
    
    This event should only be sent if the client has passed the value true for the
    'supportsProgressReporting' capability of the 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "progressUpdate"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "progressId": {
                    "type": "string",
                    "description": "The ID that was introduced in the initial 'progressStart' event."
                },
                "message": {
                    "type": "string",
                    "description": "Optional, more detailed progress message. If omitted, the previous message (if any) is used."
                },
                "percentage": {
                    "type": "number",
                    "description": "Optional progress percentage to display (value range: 0 to 100). If omitted no percentage will be shown."
                }
            },
            "required": [
                "progressId"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ProgressUpdateEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'progressUpdate'
        if body is None:
            self.body = ProgressUpdateEventBody()
        else:
            self.body = ProgressUpdateEventBody(**body) if body.__class__ !=  ProgressUpdateEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ProgressEndEvent(BaseSchema):
    """
    The event signals the end of the progress reporting with an optional final message.
    
    This event should only be sent if the client has passed the value true for the
    'supportsProgressReporting' capability of the 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "progressEnd"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "progressId": {
                    "type": "string",
                    "description": "The ID that was introduced in the initial 'ProgressStartEvent'."
                },
                "message": {
                    "type": "string",
                    "description": "Optional, more detailed progress message. If omitted, the previous message (if any) is used."
                }
            },
            "required": [
                "progressId"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param ProgressEndEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'progressEnd'
        if body is None:
            self.body = ProgressEndEventBody()
        else:
            self.body = ProgressEndEventBody(**body) if body.__class__ !=  ProgressEndEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class InvalidatedEvent(BaseSchema):
    """
    This event signals that some state in the debug adapter has changed and requires that the client
    needs to re-render the data snapshot previously requested.
    
    Debug adapters do not have to emit this event for runtime changes like stopped or thread events
    because in that case the client refetches the new state anyway. But the event can be used for
    example to refresh the UI after rendering formatting has changed in the debug adapter.
    
    This event should only be sent if the debug adapter has received a value true for the
    'supportsInvalidatedEvent' capability of the 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "event"
            ]
        },
        "event": {
            "type": "string",
            "enum": [
                "invalidated"
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "areas": {
                    "type": "array",
                    "description": "Optional set of logical areas that got invalidated. This property has a hint characteristic: a client can only be expected to make a 'best effort' in honouring the areas but there are no guarantees. If this property is missing, empty, or if values are not understand the client should assume a single value 'all'.",
                    "items": {
                        "$ref": "#/definitions/InvalidatedAreas"
                    }
                },
                "threadId": {
                    "type": "number",
                    "description": "If specified, the client only needs to refetch data related to this thread."
                },
                "stackFrameId": {
                    "type": "number",
                    "description": "If specified, the client only needs to refetch data related to this stack frame (and the 'threadId' is ignored)."
                }
            }
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, body, seq=-1, **kwargs):
        """
        :param string type: 
        :param string event: 
        :param InvalidatedEventBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'event'
        self.event = 'invalidated'
        if body is None:
            self.body = InvalidatedEventBody()
        else:
            self.body = InvalidatedEventBody(**body) if body.__class__ !=  InvalidatedEventBody else body
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'event': self.event,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register_request('runInTerminal')
@register
class RunInTerminalRequest(BaseSchema):
    """
    This optional request is sent from the debug adapter to the client to run a command in a terminal.
    
    This is typically used to launch the debuggee in a terminal provided by the client.
    
    This request should only be called if the client has passed the value true for the
    'supportsRunInTerminalRequest' capability of the 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "runInTerminal"
            ]
        },
        "arguments": {
            "type": "RunInTerminalRequestArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param RunInTerminalRequestArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'runInTerminal'
        if arguments is None:
            self.arguments = RunInTerminalRequestArguments()
        else:
            self.arguments = RunInTerminalRequestArguments(**arguments) if arguments.__class__ !=  RunInTerminalRequestArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class RunInTerminalRequestArguments(BaseSchema):
    """
    Arguments for 'runInTerminal' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "kind": {
            "type": "string",
            "enum": [
                "integrated",
                "external"
            ],
            "description": "What kind of terminal to launch."
        },
        "title": {
            "type": "string",
            "description": "Optional title of the terminal."
        },
        "cwd": {
            "type": "string",
            "description": "Working directory of the command."
        },
        "args": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of arguments. The first argument is the command to run."
        },
        "env": {
            "type": "object",
            "description": "Environment key-value pairs that are added to or removed from the default environment.",
            "additionalProperties": {
                "type": [
                    "string",
                    "null"
                ],
                "description": "Proper values must be strings. A value of 'null' removes the variable from the environment."
            }
        }
    }
    __refs__ = {'env'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, cwd, args, kind=None, title=None, env=None, **kwargs):
        """
        :param string cwd: Working directory of the command.
        :param array args: List of arguments. The first argument is the command to run.
        :param string kind: What kind of terminal to launch.
        :param string title: Optional title of the terminal.
        :param RunInTerminalRequestArgumentsEnv env: Environment key-value pairs that are added to or removed from the default environment.
        """
        self.cwd = cwd
        self.args = args
        self.kind = kind
        self.title = title
        if env is None:
            self.env = RunInTerminalRequestArgumentsEnv()
        else:
            self.env = RunInTerminalRequestArgumentsEnv(**env) if env.__class__ !=  RunInTerminalRequestArgumentsEnv else env
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'cwd': self.cwd,
             'args': self.args,
        }
        if self.kind is not None:
            dct['kind'] = self.kind
        if self.title is not None:
            dct['title'] = self.title
        if self.env is not None:
            dct['env'] = self.env.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('runInTerminal')
@register
class RunInTerminalResponse(BaseSchema):
    """
    Response to 'runInTerminal' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "processId": {
                    "type": "integer",
                    "description": "The process ID. The value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "shellProcessId": {
                    "type": "integer",
                    "description": "The process ID of the terminal shell. The value should be less than or equal to 2147483647 (2^31 - 1)."
                }
            }
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param RunInTerminalResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = RunInTerminalResponseBody()
        else:
            self.body = RunInTerminalResponseBody(**body) if body.__class__ !=  RunInTerminalResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('initialize')
@register
class InitializeRequest(BaseSchema):
    """
    The 'initialize' request is sent as the first request from the client to the debug adapter
    
    in order to configure it with client capabilities and to retrieve capabilities from the debug
    adapter.
    
    Until the debug adapter has responded to with an 'initialize' response, the client must not send any
    additional requests or events to the debug adapter.
    
    In addition the debug adapter is not allowed to send any requests or events to the client until it
    has responded with an 'initialize' response.
    
    The 'initialize' request may only be sent once.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "initialize"
            ]
        },
        "arguments": {
            "type": "InitializeRequestArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param InitializeRequestArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'initialize'
        if arguments is None:
            self.arguments = InitializeRequestArguments()
        else:
            self.arguments = InitializeRequestArguments(**arguments) if arguments.__class__ !=  InitializeRequestArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class InitializeRequestArguments(BaseSchema):
    """
    Arguments for 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "clientID": {
            "type": "string",
            "description": "The ID of the (frontend) client using this adapter."
        },
        "clientName": {
            "type": "string",
            "description": "The human readable name of the (frontend) client using this adapter."
        },
        "adapterID": {
            "type": "string",
            "description": "The ID of the debug adapter."
        },
        "locale": {
            "type": "string",
            "description": "The ISO-639 locale of the (frontend) client using this adapter, e.g. en-US or de-CH."
        },
        "linesStartAt1": {
            "type": "boolean",
            "description": "If true all line numbers are 1-based (default)."
        },
        "columnsStartAt1": {
            "type": "boolean",
            "description": "If true all column numbers are 1-based (default)."
        },
        "pathFormat": {
            "type": "string",
            "_enum": [
                "path",
                "uri"
            ],
            "description": "Determines in what format paths are specified. The default is 'path', which is the native format."
        },
        "supportsVariableType": {
            "type": "boolean",
            "description": "Client supports the optional type attribute for variables."
        },
        "supportsVariablePaging": {
            "type": "boolean",
            "description": "Client supports the paging of variables."
        },
        "supportsRunInTerminalRequest": {
            "type": "boolean",
            "description": "Client supports the runInTerminal request."
        },
        "supportsMemoryReferences": {
            "type": "boolean",
            "description": "Client supports memory references."
        },
        "supportsProgressReporting": {
            "type": "boolean",
            "description": "Client supports progress reporting."
        },
        "supportsInvalidatedEvent": {
            "type": "boolean",
            "description": "Client supports the invalidated event."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, adapterID, clientID=None, clientName=None, locale=None, linesStartAt1=None, columnsStartAt1=None, pathFormat=None, supportsVariableType=None, supportsVariablePaging=None, supportsRunInTerminalRequest=None, supportsMemoryReferences=None, supportsProgressReporting=None, supportsInvalidatedEvent=None, **kwargs):
        """
        :param string adapterID: The ID of the debug adapter.
        :param string clientID: The ID of the (frontend) client using this adapter.
        :param string clientName: The human readable name of the (frontend) client using this adapter.
        :param string locale: The ISO-639 locale of the (frontend) client using this adapter, e.g. en-US or de-CH.
        :param boolean linesStartAt1: If true all line numbers are 1-based (default).
        :param boolean columnsStartAt1: If true all column numbers are 1-based (default).
        :param string pathFormat: Determines in what format paths are specified. The default is 'path', which is the native format.
        :param boolean supportsVariableType: Client supports the optional type attribute for variables.
        :param boolean supportsVariablePaging: Client supports the paging of variables.
        :param boolean supportsRunInTerminalRequest: Client supports the runInTerminal request.
        :param boolean supportsMemoryReferences: Client supports memory references.
        :param boolean supportsProgressReporting: Client supports progress reporting.
        :param boolean supportsInvalidatedEvent: Client supports the invalidated event.
        """
        self.adapterID = adapterID
        self.clientID = clientID
        self.clientName = clientName
        self.locale = locale
        self.linesStartAt1 = linesStartAt1
        self.columnsStartAt1 = columnsStartAt1
        self.pathFormat = pathFormat
        self.supportsVariableType = supportsVariableType
        self.supportsVariablePaging = supportsVariablePaging
        self.supportsRunInTerminalRequest = supportsRunInTerminalRequest
        self.supportsMemoryReferences = supportsMemoryReferences
        self.supportsProgressReporting = supportsProgressReporting
        self.supportsInvalidatedEvent = supportsInvalidatedEvent
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'adapterID': self.adapterID,
        }
        if self.clientID is not None:
            dct['clientID'] = self.clientID
        if self.clientName is not None:
            dct['clientName'] = self.clientName
        if self.locale is not None:
            dct['locale'] = self.locale
        if self.linesStartAt1 is not None:
            dct['linesStartAt1'] = self.linesStartAt1
        if self.columnsStartAt1 is not None:
            dct['columnsStartAt1'] = self.columnsStartAt1
        if self.pathFormat is not None:
            dct['pathFormat'] = self.pathFormat
        if self.supportsVariableType is not None:
            dct['supportsVariableType'] = self.supportsVariableType
        if self.supportsVariablePaging is not None:
            dct['supportsVariablePaging'] = self.supportsVariablePaging
        if self.supportsRunInTerminalRequest is not None:
            dct['supportsRunInTerminalRequest'] = self.supportsRunInTerminalRequest
        if self.supportsMemoryReferences is not None:
            dct['supportsMemoryReferences'] = self.supportsMemoryReferences
        if self.supportsProgressReporting is not None:
            dct['supportsProgressReporting'] = self.supportsProgressReporting
        if self.supportsInvalidatedEvent is not None:
            dct['supportsInvalidatedEvent'] = self.supportsInvalidatedEvent
        dct.update(self.kwargs)
        return dct


@register_response('initialize')
@register
class InitializeResponse(BaseSchema):
    """
    Response to 'initialize' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "description": "The capabilities of this debug adapter.",
            "type": "Capabilities"
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param Capabilities body: The capabilities of this debug adapter.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        if body is None:
            self.body = Capabilities()
        else:
            self.body = Capabilities(**body) if body.__class__ !=  Capabilities else body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body.to_dict()
        dct.update(self.kwargs)
        return dct


@register_request('configurationDone')
@register
class ConfigurationDoneRequest(BaseSchema):
    """
    This optional request indicates that the client has finished initialization of the debug adapter.
    
    So it is the last request in the sequence of configuration requests (which was started by the
    'initialized' event).
    
    Clients should only call this request if the capability 'supportsConfigurationDoneRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "configurationDone"
            ]
        },
        "arguments": {
            "type": "ConfigurationDoneArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param ConfigurationDoneArguments arguments: 
        """
        self.type = 'request'
        self.command = 'configurationDone'
        self.seq = seq
        if arguments is None:
            self.arguments = ConfigurationDoneArguments()
        else:
            self.arguments = ConfigurationDoneArguments(**arguments) if arguments.__class__ !=  ConfigurationDoneArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class ConfigurationDoneArguments(BaseSchema):
    """
    Arguments for 'configurationDone' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register_response('configurationDone')
@register
class ConfigurationDoneResponse(BaseSchema):
    """
    Response to 'configurationDone' request. This is just an acknowledgement, so no body field is
    required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('launch')
@register
class LaunchRequest(BaseSchema):
    """
    This launch request is sent from the client to the debug adapter to start the debuggee with or
    without debugging (if 'noDebug' is true).
    
    Since launching is debugger/runtime specific, the arguments for this request are not part of this
    specification.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "launch"
            ]
        },
        "arguments": {
            "type": "LaunchRequestArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param LaunchRequestArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'launch'
        if arguments is None:
            self.arguments = LaunchRequestArguments()
        else:
            self.arguments = LaunchRequestArguments(**arguments) if arguments.__class__ !=  LaunchRequestArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class LaunchRequestArguments(BaseSchema):
    """
    Arguments for 'launch' request. Additional attributes are implementation specific.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "noDebug": {
            "type": "boolean",
            "description": "If noDebug is true the launch request should launch the program without enabling debugging."
        },
        "__restart": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Optional data from the previous, restarted session.\nThe data is sent as the 'restart' attribute of the 'terminated' event.\nThe client should leave the data intact."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, noDebug=None, __restart=None, **kwargs):
        """
        :param boolean noDebug: If noDebug is true the launch request should launch the program without enabling debugging.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] __restart: Optional data from the previous, restarted session.
        The data is sent as the 'restart' attribute of the 'terminated' event.
        The client should leave the data intact.
        """
        self.noDebug = noDebug
        self.__restart = __restart
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.noDebug is not None:
            dct['noDebug'] = self.noDebug
        if self.__restart is not None:
            dct['__restart'] = self.__restart
        dct.update(self.kwargs)
        return dct


@register_response('launch')
@register
class LaunchResponse(BaseSchema):
    """
    Response to 'launch' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('attach')
@register
class AttachRequest(BaseSchema):
    """
    The attach request is sent from the client to the debug adapter to attach to a debuggee that is
    already running.
    
    Since attaching is debugger/runtime specific, the arguments for this request are not part of this
    specification.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "attach"
            ]
        },
        "arguments": {
            "type": "AttachRequestArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param AttachRequestArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'attach'
        if arguments is None:
            self.arguments = AttachRequestArguments()
        else:
            self.arguments = AttachRequestArguments(**arguments) if arguments.__class__ !=  AttachRequestArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class AttachRequestArguments(BaseSchema):
    """
    Arguments for 'attach' request. Additional attributes are implementation specific.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "__restart": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Optional data from the previous, restarted session.\nThe data is sent as the 'restart' attribute of the 'terminated' event.\nThe client should leave the data intact."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, __restart=None, **kwargs):
        """
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] __restart: Optional data from the previous, restarted session.
        The data is sent as the 'restart' attribute of the 'terminated' event.
        The client should leave the data intact.
        """
        self.__restart = __restart
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.__restart is not None:
            dct['__restart'] = self.__restart
        dct.update(self.kwargs)
        return dct


@register_response('attach')
@register
class AttachResponse(BaseSchema):
    """
    Response to 'attach' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('restart')
@register
class RestartRequest(BaseSchema):
    """
    Restarts a debug session. Clients should only call this request if the capability
    'supportsRestartRequest' is true.
    
    If the capability is missing or has the value false, a typical client will emulate 'restart' by
    terminating the debug adapter first and then launching it anew.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "restart"
            ]
        },
        "arguments": {
            "type": "RestartArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param RestartArguments arguments: 
        """
        self.type = 'request'
        self.command = 'restart'
        self.seq = seq
        if arguments is None:
            self.arguments = RestartArguments()
        else:
            self.arguments = RestartArguments(**arguments) if arguments.__class__ !=  RestartArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class RestartArguments(BaseSchema):
    """
    Arguments for 'restart' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register_response('restart')
@register
class RestartResponse(BaseSchema):
    """
    Response to 'restart' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('disconnect')
@register
class DisconnectRequest(BaseSchema):
    """
    The 'disconnect' request is sent from the client to the debug adapter in order to stop debugging.
    
    It asks the debug adapter to disconnect from the debuggee and to terminate the debug adapter.
    
    If the debuggee has been started with the 'launch' request, the 'disconnect' request terminates the
    debuggee.
    
    If the 'attach' request was used to connect to the debuggee, 'disconnect' does not terminate the
    debuggee.
    
    This behavior can be controlled with the 'terminateDebuggee' argument (if supported by the debug
    adapter).

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "disconnect"
            ]
        },
        "arguments": {
            "type": "DisconnectArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param DisconnectArguments arguments: 
        """
        self.type = 'request'
        self.command = 'disconnect'
        self.seq = seq
        if arguments is None:
            self.arguments = DisconnectArguments()
        else:
            self.arguments = DisconnectArguments(**arguments) if arguments.__class__ !=  DisconnectArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class DisconnectArguments(BaseSchema):
    """
    Arguments for 'disconnect' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "restart": {
            "type": "boolean",
            "description": "A value of true indicates that this 'disconnect' request is part of a restart sequence."
        },
        "terminateDebuggee": {
            "type": "boolean",
            "description": "Indicates whether the debuggee should be terminated when the debugger is disconnected.\nIf unspecified, the debug adapter is free to do whatever it thinks is best.\nThe attribute is only honored by a debug adapter if the capability 'supportTerminateDebuggee' is true."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, restart=None, terminateDebuggee=None, **kwargs):
        """
        :param boolean restart: A value of true indicates that this 'disconnect' request is part of a restart sequence.
        :param boolean terminateDebuggee: Indicates whether the debuggee should be terminated when the debugger is disconnected.
        If unspecified, the debug adapter is free to do whatever it thinks is best.
        The attribute is only honored by a debug adapter if the capability 'supportTerminateDebuggee' is true.
        """
        self.restart = restart
        self.terminateDebuggee = terminateDebuggee
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.restart is not None:
            dct['restart'] = self.restart
        if self.terminateDebuggee is not None:
            dct['terminateDebuggee'] = self.terminateDebuggee
        dct.update(self.kwargs)
        return dct


@register_response('disconnect')
@register
class DisconnectResponse(BaseSchema):
    """
    Response to 'disconnect' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('terminate')
@register
class TerminateRequest(BaseSchema):
    """
    The 'terminate' request is sent from the client to the debug adapter in order to give the debuggee a
    chance for terminating itself.
    
    Clients should only call this request if the capability 'supportsTerminateRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "terminate"
            ]
        },
        "arguments": {
            "type": "TerminateArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param TerminateArguments arguments: 
        """
        self.type = 'request'
        self.command = 'terminate'
        self.seq = seq
        if arguments is None:
            self.arguments = TerminateArguments()
        else:
            self.arguments = TerminateArguments(**arguments) if arguments.__class__ !=  TerminateArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class TerminateArguments(BaseSchema):
    """
    Arguments for 'terminate' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "restart": {
            "type": "boolean",
            "description": "A value of true indicates that this 'terminate' request is part of a restart sequence."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, restart=None, **kwargs):
        """
        :param boolean restart: A value of true indicates that this 'terminate' request is part of a restart sequence.
        """
        self.restart = restart
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.restart is not None:
            dct['restart'] = self.restart
        dct.update(self.kwargs)
        return dct


@register_response('terminate')
@register
class TerminateResponse(BaseSchema):
    """
    Response to 'terminate' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('breakpointLocations')
@register
class BreakpointLocationsRequest(BaseSchema):
    """
    The 'breakpointLocations' request returns all possible locations for source breakpoints in a given
    range.
    
    Clients should only call this request if the capability 'supportsBreakpointLocationsRequest' is
    true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "breakpointLocations"
            ]
        },
        "arguments": {
            "type": "BreakpointLocationsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param BreakpointLocationsArguments arguments: 
        """
        self.type = 'request'
        self.command = 'breakpointLocations'
        self.seq = seq
        if arguments is None:
            self.arguments = BreakpointLocationsArguments()
        else:
            self.arguments = BreakpointLocationsArguments(**arguments) if arguments.__class__ !=  BreakpointLocationsArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class BreakpointLocationsArguments(BaseSchema):
    """
    Arguments for 'breakpointLocations' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "source": {
            "description": "The source location of the breakpoints; either 'source.path' or 'source.reference' must be specified.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "Start line of range to search possible breakpoint locations in. If only the line is specified, the request returns all possible locations in that line."
        },
        "column": {
            "type": "integer",
            "description": "Optional start column of range to search possible breakpoint locations in. If no start column is given, the first column in the start line is assumed."
        },
        "endLine": {
            "type": "integer",
            "description": "Optional end line of range to search possible breakpoint locations in. If no end line is given, then the end line is assumed to be the start line."
        },
        "endColumn": {
            "type": "integer",
            "description": "Optional end column of range to search possible breakpoint locations in. If no end column is given, then it is assumed to be in the last column of the end line."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, source, line, column=None, endLine=None, endColumn=None, **kwargs):
        """
        :param Source source: The source location of the breakpoints; either 'source.path' or 'source.reference' must be specified.
        :param integer line: Start line of range to search possible breakpoint locations in. If only the line is specified, the request returns all possible locations in that line.
        :param integer column: Optional start column of range to search possible breakpoint locations in. If no start column is given, the first column in the start line is assumed.
        :param integer endLine: Optional end line of range to search possible breakpoint locations in. If no end line is given, then the end line is assumed to be the start line.
        :param integer endColumn: Optional end column of range to search possible breakpoint locations in. If no end column is given, then it is assumed to be in the last column of the end line.
        """
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'source': self.source.to_dict(),
             'line': self.line,
        }
        if self.column is not None:
            dct['column'] = self.column
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        dct.update(self.kwargs)
        return dct


@register_response('breakpointLocations')
@register
class BreakpointLocationsResponse(BaseSchema):
    """
    Response to 'breakpointLocations' request.
    
    Contains possible locations for source breakpoints.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "breakpoints": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/BreakpointLocation"
                    },
                    "description": "Sorted set of possible breakpoint locations."
                }
            },
            "required": [
                "breakpoints"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param BreakpointLocationsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = BreakpointLocationsResponseBody()
        else:
            self.body = BreakpointLocationsResponseBody(**body) if body.__class__ !=  BreakpointLocationsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setBreakpoints')
@register
class SetBreakpointsRequest(BaseSchema):
    """
    Sets multiple breakpoints for a single source and clears all previous breakpoints in that source.
    
    To clear all breakpoint for a source, specify an empty array.
    
    When a breakpoint is hit, a 'stopped' event (with reason 'breakpoint') is generated.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setBreakpoints"
            ]
        },
        "arguments": {
            "type": "SetBreakpointsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetBreakpointsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setBreakpoints'
        if arguments is None:
            self.arguments = SetBreakpointsArguments()
        else:
            self.arguments = SetBreakpointsArguments(**arguments) if arguments.__class__ !=  SetBreakpointsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetBreakpointsArguments(BaseSchema):
    """
    Arguments for 'setBreakpoints' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "source": {
            "description": "The source location of the breakpoints; either 'source.path' or 'source.reference' must be specified.",
            "type": "Source"
        },
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/SourceBreakpoint"
            },
            "description": "The code locations of the breakpoints."
        },
        "lines": {
            "type": "array",
            "items": {
                "type": "integer"
            },
            "description": "Deprecated: The code locations of the breakpoints."
        },
        "sourceModified": {
            "type": "boolean",
            "description": "A value of true indicates that the underlying source has been modified which results in new breakpoint locations."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, source, breakpoints=None, lines=None, sourceModified=None, **kwargs):
        """
        :param Source source: The source location of the breakpoints; either 'source.path' or 'source.reference' must be specified.
        :param array breakpoints: The code locations of the breakpoints.
        :param array lines: Deprecated: The code locations of the breakpoints.
        :param boolean sourceModified: A value of true indicates that the underlying source has been modified which results in new breakpoint locations.
        """
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.breakpoints = breakpoints
        self.lines = lines
        self.sourceModified = sourceModified
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'source': self.source.to_dict(),
        }
        if self.breakpoints is not None:
            dct['breakpoints'] = self.breakpoints
        if self.lines is not None:
            dct['lines'] = self.lines
        if self.sourceModified is not None:
            dct['sourceModified'] = self.sourceModified
        dct.update(self.kwargs)
        return dct


@register_response('setBreakpoints')
@register
class SetBreakpointsResponse(BaseSchema):
    """
    Response to 'setBreakpoints' request.
    
    Returned is information about each breakpoint created by this request.
    
    This includes the actual code location and whether the breakpoint could be verified.
    
    The breakpoints returned are in the same order as the elements of the 'breakpoints'
    
    (or the deprecated 'lines') array in the arguments.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "breakpoints": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Breakpoint"
                    },
                    "description": "Information about the breakpoints.\nThe array elements are in the same order as the elements of the 'breakpoints' (or the deprecated 'lines') array in the arguments."
                }
            },
            "required": [
                "breakpoints"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SetBreakpointsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SetBreakpointsResponseBody()
        else:
            self.body = SetBreakpointsResponseBody(**body) if body.__class__ !=  SetBreakpointsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setFunctionBreakpoints')
@register
class SetFunctionBreakpointsRequest(BaseSchema):
    """
    Replaces all existing function breakpoints with new function breakpoints.
    
    To clear all function breakpoints, specify an empty array.
    
    When a function breakpoint is hit, a 'stopped' event (with reason 'function breakpoint') is
    generated.
    
    Clients should only call this request if the capability 'supportsFunctionBreakpoints' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setFunctionBreakpoints"
            ]
        },
        "arguments": {
            "type": "SetFunctionBreakpointsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetFunctionBreakpointsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setFunctionBreakpoints'
        if arguments is None:
            self.arguments = SetFunctionBreakpointsArguments()
        else:
            self.arguments = SetFunctionBreakpointsArguments(**arguments) if arguments.__class__ !=  SetFunctionBreakpointsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetFunctionBreakpointsArguments(BaseSchema):
    """
    Arguments for 'setFunctionBreakpoints' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/FunctionBreakpoint"
            },
            "description": "The function names of the breakpoints."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: The function names of the breakpoints.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register_response('setFunctionBreakpoints')
@register
class SetFunctionBreakpointsResponse(BaseSchema):
    """
    Response to 'setFunctionBreakpoints' request.
    
    Returned is information about each breakpoint created by this request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "breakpoints": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Breakpoint"
                    },
                    "description": "Information about the breakpoints. The array elements correspond to the elements of the 'breakpoints' array."
                }
            },
            "required": [
                "breakpoints"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SetFunctionBreakpointsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SetFunctionBreakpointsResponseBody()
        else:
            self.body = SetFunctionBreakpointsResponseBody(**body) if body.__class__ !=  SetFunctionBreakpointsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setExceptionBreakpoints')
@register
class SetExceptionBreakpointsRequest(BaseSchema):
    """
    The request configures the debuggers response to thrown exceptions.
    
    If an exception is configured to break, a 'stopped' event is fired (with reason 'exception').
    
    Clients should only call this request if the capability 'exceptionBreakpointFilters' returns one or
    more filters.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setExceptionBreakpoints"
            ]
        },
        "arguments": {
            "type": "SetExceptionBreakpointsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetExceptionBreakpointsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setExceptionBreakpoints'
        if arguments is None:
            self.arguments = SetExceptionBreakpointsArguments()
        else:
            self.arguments = SetExceptionBreakpointsArguments(**arguments) if arguments.__class__ !=  SetExceptionBreakpointsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetExceptionBreakpointsArguments(BaseSchema):
    """
    Arguments for 'setExceptionBreakpoints' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "filters": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "IDs of checked exception options. The set of IDs is returned via the 'exceptionBreakpointFilters' capability."
        },
        "exceptionOptions": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ExceptionOptions"
            },
            "description": "Configuration options for selected exceptions.\nThe attribute is only honored by a debug adapter if the capability 'supportsExceptionOptions' is true."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, filters, exceptionOptions=None, **kwargs):
        """
        :param array filters: IDs of checked exception options. The set of IDs is returned via the 'exceptionBreakpointFilters' capability.
        :param array exceptionOptions: Configuration options for selected exceptions.
        The attribute is only honored by a debug adapter if the capability 'supportsExceptionOptions' is true.
        """
        self.filters = filters
        self.exceptionOptions = exceptionOptions
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'filters': self.filters,
        }
        if self.exceptionOptions is not None:
            dct['exceptionOptions'] = self.exceptionOptions
        dct.update(self.kwargs)
        return dct


@register_response('setExceptionBreakpoints')
@register
class SetExceptionBreakpointsResponse(BaseSchema):
    """
    Response to 'setExceptionBreakpoints' request. This is just an acknowledgement, so no body field is
    required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('dataBreakpointInfo')
@register
class DataBreakpointInfoRequest(BaseSchema):
    """
    Obtains information on a possible data breakpoint that could be set on an expression or variable.
    
    Clients should only call this request if the capability 'supportsDataBreakpoints' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "dataBreakpointInfo"
            ]
        },
        "arguments": {
            "type": "DataBreakpointInfoArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param DataBreakpointInfoArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'dataBreakpointInfo'
        if arguments is None:
            self.arguments = DataBreakpointInfoArguments()
        else:
            self.arguments = DataBreakpointInfoArguments(**arguments) if arguments.__class__ !=  DataBreakpointInfoArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class DataBreakpointInfoArguments(BaseSchema):
    """
    Arguments for 'dataBreakpointInfo' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "variablesReference": {
            "type": "integer",
            "description": "Reference to the Variable container if the data breakpoint is requested for a child of the container."
        },
        "name": {
            "type": "string",
            "description": "The name of the Variable's child to obtain data breakpoint information for.\nIf variableReference isn\u2019t provided, this can be an expression."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, name, variablesReference=None, **kwargs):
        """
        :param string name: The name of the Variable's child to obtain data breakpoint information for.
        If variableReference isn’t provided, this can be an expression.
        :param integer variablesReference: Reference to the Variable container if the data breakpoint is requested for a child of the container.
        """
        self.name = name
        self.variablesReference = variablesReference
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'name': self.name,
        }
        if self.variablesReference is not None:
            dct['variablesReference'] = self.variablesReference
        dct.update(self.kwargs)
        return dct


@register_response('dataBreakpointInfo')
@register
class DataBreakpointInfoResponse(BaseSchema):
    """
    Response to 'dataBreakpointInfo' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "dataId": {
                    "type": [
                        "string",
                        "null"
                    ],
                    "description": "An identifier for the data on which a data breakpoint can be registered with the setDataBreakpoints request or null if no data breakpoint is available."
                },
                "description": {
                    "type": "string",
                    "description": "UI string that describes on what data the breakpoint is set on or why a data breakpoint is not available."
                },
                "accessTypes": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/DataBreakpointAccessType"
                    },
                    "description": "Optional attribute listing the available access types for a potential data breakpoint. A UI frontend could surface this information."
                },
                "canPersist": {
                    "type": "boolean",
                    "description": "Optional attribute indicating that a potential data breakpoint could be persisted across sessions."
                }
            },
            "required": [
                "dataId",
                "description"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param DataBreakpointInfoResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = DataBreakpointInfoResponseBody()
        else:
            self.body = DataBreakpointInfoResponseBody(**body) if body.__class__ !=  DataBreakpointInfoResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setDataBreakpoints')
@register
class SetDataBreakpointsRequest(BaseSchema):
    """
    Replaces all existing data breakpoints with new data breakpoints.
    
    To clear all data breakpoints, specify an empty array.
    
    When a data breakpoint is hit, a 'stopped' event (with reason 'data breakpoint') is generated.
    
    Clients should only call this request if the capability 'supportsDataBreakpoints' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setDataBreakpoints"
            ]
        },
        "arguments": {
            "type": "SetDataBreakpointsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetDataBreakpointsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setDataBreakpoints'
        if arguments is None:
            self.arguments = SetDataBreakpointsArguments()
        else:
            self.arguments = SetDataBreakpointsArguments(**arguments) if arguments.__class__ !=  SetDataBreakpointsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetDataBreakpointsArguments(BaseSchema):
    """
    Arguments for 'setDataBreakpoints' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/DataBreakpoint"
            },
            "description": "The contents of this array replaces all existing data breakpoints. An empty array clears all data breakpoints."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: The contents of this array replaces all existing data breakpoints. An empty array clears all data breakpoints.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register_response('setDataBreakpoints')
@register
class SetDataBreakpointsResponse(BaseSchema):
    """
    Response to 'setDataBreakpoints' request.
    
    Returned is information about each breakpoint created by this request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "breakpoints": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Breakpoint"
                    },
                    "description": "Information about the data breakpoints. The array elements correspond to the elements of the input argument 'breakpoints' array."
                }
            },
            "required": [
                "breakpoints"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SetDataBreakpointsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SetDataBreakpointsResponseBody()
        else:
            self.body = SetDataBreakpointsResponseBody(**body) if body.__class__ !=  SetDataBreakpointsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setInstructionBreakpoints')
@register
class SetInstructionBreakpointsRequest(BaseSchema):
    """
    Replaces all existing instruction breakpoints. Typically, instruction breakpoints would be set from
    a diassembly window.
    
    To clear all instruction breakpoints, specify an empty array.
    
    When an instruction breakpoint is hit, a 'stopped' event (with reason 'instruction breakpoint') is
    generated.
    
    Clients should only call this request if the capability 'supportsInstructionBreakpoints' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setInstructionBreakpoints"
            ]
        },
        "arguments": {
            "type": "SetInstructionBreakpointsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetInstructionBreakpointsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setInstructionBreakpoints'
        if arguments is None:
            self.arguments = SetInstructionBreakpointsArguments()
        else:
            self.arguments = SetInstructionBreakpointsArguments(**arguments) if arguments.__class__ !=  SetInstructionBreakpointsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetInstructionBreakpointsArguments(BaseSchema):
    """
    Arguments for 'setInstructionBreakpoints' request

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/InstructionBreakpoint"
            },
            "description": "The instruction references of the breakpoints"
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: The instruction references of the breakpoints
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register_response('setInstructionBreakpoints')
@register
class SetInstructionBreakpointsResponse(BaseSchema):
    """
    Response to 'setInstructionBreakpoints' request

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "breakpoints": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Breakpoint"
                    },
                    "description": "Information about the breakpoints. The array elements correspond to the elements of the 'breakpoints' array."
                }
            },
            "required": [
                "breakpoints"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SetInstructionBreakpointsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SetInstructionBreakpointsResponseBody()
        else:
            self.body = SetInstructionBreakpointsResponseBody(**body) if body.__class__ !=  SetInstructionBreakpointsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('continue')
@register
class ContinueRequest(BaseSchema):
    """
    The request starts the debuggee to run again.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "continue"
            ]
        },
        "arguments": {
            "type": "ContinueArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param ContinueArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'continue'
        if arguments is None:
            self.arguments = ContinueArguments()
        else:
            self.arguments = ContinueArguments(**arguments) if arguments.__class__ !=  ContinueArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ContinueArguments(BaseSchema):
    """
    Arguments for 'continue' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Continue execution for the specified thread (if possible).\nIf the backend cannot continue on a single thread but will continue on all threads, it should set the 'allThreadsContinued' attribute in the response to true."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, **kwargs):
        """
        :param integer threadId: Continue execution for the specified thread (if possible).
        If the backend cannot continue on a single thread but will continue on all threads, it should set the 'allThreadsContinued' attribute in the response to true.
        """
        self.threadId = threadId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('continue')
@register
class ContinueResponse(BaseSchema):
    """
    Response to 'continue' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "allThreadsContinued": {
                    "type": "boolean",
                    "description": "If true, the 'continue' request has ignored the specified thread and continued all threads instead.\nIf this attribute is missing a value of 'true' is assumed for backward compatibility."
                }
            }
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param ContinueResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = ContinueResponseBody()
        else:
            self.body = ContinueResponseBody(**body) if body.__class__ !=  ContinueResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('next')
@register
class NextRequest(BaseSchema):
    """
    The request starts the debuggee to run again for one step.
    
    The debug adapter first sends the response and then a 'stopped' event (with reason 'step') after the
    step has completed.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "next"
            ]
        },
        "arguments": {
            "type": "NextArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param NextArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'next'
        if arguments is None:
            self.arguments = NextArguments()
        else:
            self.arguments = NextArguments(**arguments) if arguments.__class__ !=  NextArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class NextArguments(BaseSchema):
    """
    Arguments for 'next' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Execute 'next' for this thread."
        },
        "granularity": {
            "description": "Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.",
            "type": "SteppingGranularity"
        }
    }
    __refs__ = {'granularity'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, granularity=None, **kwargs):
        """
        :param integer threadId: Execute 'next' for this thread.
        :param SteppingGranularity granularity: Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.
        """
        self.threadId = threadId
        if granularity is None:
            self.granularity = SteppingGranularity()
        else:
            self.granularity = SteppingGranularity(**kwargs) if granularity.__class__ !=  SteppingGranularity else granularity
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        if self.granularity is not None:
            dct['granularity'] = self.granularity.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('next')
@register
class NextResponse(BaseSchema):
    """
    Response to 'next' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('stepIn')
@register
class StepInRequest(BaseSchema):
    """
    The request starts the debuggee to step into a function/method if possible.
    
    If it cannot step into a target, 'stepIn' behaves like 'next'.
    
    The debug adapter first sends the response and then a 'stopped' event (with reason 'step') after the
    step has completed.
    
    If there are multiple function/method calls (or other targets) on the source line,
    
    the optional argument 'targetId' can be used to control into which target the 'stepIn' should occur.
    
    The list of possible targets for a given source line can be retrieved via the 'stepInTargets'
    request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "stepIn"
            ]
        },
        "arguments": {
            "type": "StepInArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param StepInArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'stepIn'
        if arguments is None:
            self.arguments = StepInArguments()
        else:
            self.arguments = StepInArguments(**arguments) if arguments.__class__ !=  StepInArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class StepInArguments(BaseSchema):
    """
    Arguments for 'stepIn' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Execute 'stepIn' for this thread."
        },
        "targetId": {
            "type": "integer",
            "description": "Optional id of the target to step into."
        },
        "granularity": {
            "description": "Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.",
            "type": "SteppingGranularity"
        }
    }
    __refs__ = {'granularity'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, targetId=None, granularity=None, **kwargs):
        """
        :param integer threadId: Execute 'stepIn' for this thread.
        :param integer targetId: Optional id of the target to step into.
        :param SteppingGranularity granularity: Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.
        """
        self.threadId = threadId
        self.targetId = targetId
        if granularity is None:
            self.granularity = SteppingGranularity()
        else:
            self.granularity = SteppingGranularity(**kwargs) if granularity.__class__ !=  SteppingGranularity else granularity
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        if self.targetId is not None:
            dct['targetId'] = self.targetId
        if self.granularity is not None:
            dct['granularity'] = self.granularity.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('stepIn')
@register
class StepInResponse(BaseSchema):
    """
    Response to 'stepIn' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('stepOut')
@register
class StepOutRequest(BaseSchema):
    """
    The request starts the debuggee to run again for one step.
    
    The debug adapter first sends the response and then a 'stopped' event (with reason 'step') after the
    step has completed.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "stepOut"
            ]
        },
        "arguments": {
            "type": "StepOutArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param StepOutArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'stepOut'
        if arguments is None:
            self.arguments = StepOutArguments()
        else:
            self.arguments = StepOutArguments(**arguments) if arguments.__class__ !=  StepOutArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class StepOutArguments(BaseSchema):
    """
    Arguments for 'stepOut' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Execute 'stepOut' for this thread."
        },
        "granularity": {
            "description": "Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.",
            "type": "SteppingGranularity"
        }
    }
    __refs__ = {'granularity'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, granularity=None, **kwargs):
        """
        :param integer threadId: Execute 'stepOut' for this thread.
        :param SteppingGranularity granularity: Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.
        """
        self.threadId = threadId
        if granularity is None:
            self.granularity = SteppingGranularity()
        else:
            self.granularity = SteppingGranularity(**kwargs) if granularity.__class__ !=  SteppingGranularity else granularity
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        if self.granularity is not None:
            dct['granularity'] = self.granularity.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('stepOut')
@register
class StepOutResponse(BaseSchema):
    """
    Response to 'stepOut' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('stepBack')
@register
class StepBackRequest(BaseSchema):
    """
    The request starts the debuggee to run one step backwards.
    
    The debug adapter first sends the response and then a 'stopped' event (with reason 'step') after the
    step has completed.
    
    Clients should only call this request if the capability 'supportsStepBack' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "stepBack"
            ]
        },
        "arguments": {
            "type": "StepBackArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param StepBackArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'stepBack'
        if arguments is None:
            self.arguments = StepBackArguments()
        else:
            self.arguments = StepBackArguments(**arguments) if arguments.__class__ !=  StepBackArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class StepBackArguments(BaseSchema):
    """
    Arguments for 'stepBack' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Execute 'stepBack' for this thread."
        },
        "granularity": {
            "description": "Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.",
            "type": "SteppingGranularity"
        }
    }
    __refs__ = {'granularity'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, granularity=None, **kwargs):
        """
        :param integer threadId: Execute 'stepBack' for this thread.
        :param SteppingGranularity granularity: Optional granularity to step. If no granularity is specified, a granularity of 'statement' is assumed.
        """
        self.threadId = threadId
        if granularity is None:
            self.granularity = SteppingGranularity()
        else:
            self.granularity = SteppingGranularity(**kwargs) if granularity.__class__ !=  SteppingGranularity else granularity
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        if self.granularity is not None:
            dct['granularity'] = self.granularity.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('stepBack')
@register
class StepBackResponse(BaseSchema):
    """
    Response to 'stepBack' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('reverseContinue')
@register
class ReverseContinueRequest(BaseSchema):
    """
    The request starts the debuggee to run backward.
    
    Clients should only call this request if the capability 'supportsStepBack' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "reverseContinue"
            ]
        },
        "arguments": {
            "type": "ReverseContinueArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param ReverseContinueArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'reverseContinue'
        if arguments is None:
            self.arguments = ReverseContinueArguments()
        else:
            self.arguments = ReverseContinueArguments(**arguments) if arguments.__class__ !=  ReverseContinueArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ReverseContinueArguments(BaseSchema):
    """
    Arguments for 'reverseContinue' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Execute 'reverseContinue' for this thread."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, **kwargs):
        """
        :param integer threadId: Execute 'reverseContinue' for this thread.
        """
        self.threadId = threadId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('reverseContinue')
@register
class ReverseContinueResponse(BaseSchema):
    """
    Response to 'reverseContinue' request. This is just an acknowledgement, so no body field is
    required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('restartFrame')
@register
class RestartFrameRequest(BaseSchema):
    """
    The request restarts execution of the specified stackframe.
    
    The debug adapter first sends the response and then a 'stopped' event (with reason 'restart') after
    the restart has completed.
    
    Clients should only call this request if the capability 'supportsRestartFrame' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "restartFrame"
            ]
        },
        "arguments": {
            "type": "RestartFrameArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param RestartFrameArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'restartFrame'
        if arguments is None:
            self.arguments = RestartFrameArguments()
        else:
            self.arguments = RestartFrameArguments(**arguments) if arguments.__class__ !=  RestartFrameArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class RestartFrameArguments(BaseSchema):
    """
    Arguments for 'restartFrame' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "frameId": {
            "type": "integer",
            "description": "Restart this stackframe."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, frameId, **kwargs):
        """
        :param integer frameId: Restart this stackframe.
        """
        self.frameId = frameId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'frameId': self.frameId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('restartFrame')
@register
class RestartFrameResponse(BaseSchema):
    """
    Response to 'restartFrame' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('goto')
@register
class GotoRequest(BaseSchema):
    """
    The request sets the location where the debuggee will continue to run.
    
    This makes it possible to skip the execution of code or to executed code again.
    
    The code between the current location and the goto target is not executed but skipped.
    
    The debug adapter first sends the response and then a 'stopped' event with reason 'goto'.
    
    Clients should only call this request if the capability 'supportsGotoTargetsRequest' is true
    (because only then goto targets exist that can be passed as arguments).

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "goto"
            ]
        },
        "arguments": {
            "type": "GotoArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param GotoArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'goto'
        if arguments is None:
            self.arguments = GotoArguments()
        else:
            self.arguments = GotoArguments(**arguments) if arguments.__class__ !=  GotoArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class GotoArguments(BaseSchema):
    """
    Arguments for 'goto' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Set the goto target for this thread."
        },
        "targetId": {
            "type": "integer",
            "description": "The location where the debuggee will continue to run."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, targetId, **kwargs):
        """
        :param integer threadId: Set the goto target for this thread.
        :param integer targetId: The location where the debuggee will continue to run.
        """
        self.threadId = threadId
        self.targetId = targetId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
             'targetId': self.targetId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('goto')
@register
class GotoResponse(BaseSchema):
    """
    Response to 'goto' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('pause')
@register
class PauseRequest(BaseSchema):
    """
    The request suspends the debuggee.
    
    The debug adapter first sends the response and then a 'stopped' event (with reason 'pause') after
    the thread has been paused successfully.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "pause"
            ]
        },
        "arguments": {
            "type": "PauseArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param PauseArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'pause'
        if arguments is None:
            self.arguments = PauseArguments()
        else:
            self.arguments = PauseArguments(**arguments) if arguments.__class__ !=  PauseArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class PauseArguments(BaseSchema):
    """
    Arguments for 'pause' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Pause execution for this thread."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, **kwargs):
        """
        :param integer threadId: Pause execution for this thread.
        """
        self.threadId = threadId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('pause')
@register
class PauseResponse(BaseSchema):
    """
    Response to 'pause' request. This is just an acknowledgement, so no body field is required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('stackTrace')
@register
class StackTraceRequest(BaseSchema):
    """
    The request returns a stacktrace from the current execution state.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "stackTrace"
            ]
        },
        "arguments": {
            "type": "StackTraceArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param StackTraceArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'stackTrace'
        if arguments is None:
            self.arguments = StackTraceArguments()
        else:
            self.arguments = StackTraceArguments(**arguments) if arguments.__class__ !=  StackTraceArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class StackTraceArguments(BaseSchema):
    """
    Arguments for 'stackTrace' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Retrieve the stacktrace for this thread."
        },
        "startFrame": {
            "type": "integer",
            "description": "The index of the first frame to return; if omitted frames start at 0."
        },
        "levels": {
            "type": "integer",
            "description": "The maximum number of frames to return. If levels is not specified or 0, all frames are returned."
        },
        "format": {
            "description": "Specifies details on how to format the stack frames.\nThe attribute is only honored by a debug adapter if the capability 'supportsValueFormattingOptions' is true.",
            "type": "StackFrameFormat"
        }
    }
    __refs__ = {'format'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, startFrame=None, levels=None, format=None, **kwargs):
        """
        :param integer threadId: Retrieve the stacktrace for this thread.
        :param integer startFrame: The index of the first frame to return; if omitted frames start at 0.
        :param integer levels: The maximum number of frames to return. If levels is not specified or 0, all frames are returned.
        :param StackFrameFormat format: Specifies details on how to format the stack frames.
        The attribute is only honored by a debug adapter if the capability 'supportsValueFormattingOptions' is true.
        """
        self.threadId = threadId
        self.startFrame = startFrame
        self.levels = levels
        if format is None:
            self.format = StackFrameFormat()
        else:
            self.format = StackFrameFormat(**format) if format.__class__ !=  StackFrameFormat else format
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        if self.startFrame is not None:
            dct['startFrame'] = self.startFrame
        if self.levels is not None:
            dct['levels'] = self.levels
        if self.format is not None:
            dct['format'] = self.format.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('stackTrace')
@register
class StackTraceResponse(BaseSchema):
    """
    Response to 'stackTrace' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "stackFrames": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/StackFrame"
                    },
                    "description": "The frames of the stackframe. If the array has length zero, there are no stackframes available.\nThis means that there is no location information available."
                },
                "totalFrames": {
                    "type": "integer",
                    "description": "The total number of frames available."
                }
            },
            "required": [
                "stackFrames"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param StackTraceResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = StackTraceResponseBody()
        else:
            self.body = StackTraceResponseBody(**body) if body.__class__ !=  StackTraceResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('scopes')
@register
class ScopesRequest(BaseSchema):
    """
    The request returns the variable scopes for a given stackframe ID.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "scopes"
            ]
        },
        "arguments": {
            "type": "ScopesArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param ScopesArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'scopes'
        if arguments is None:
            self.arguments = ScopesArguments()
        else:
            self.arguments = ScopesArguments(**arguments) if arguments.__class__ !=  ScopesArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ScopesArguments(BaseSchema):
    """
    Arguments for 'scopes' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "frameId": {
            "type": "integer",
            "description": "Retrieve the scopes for this stackframe."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, frameId, **kwargs):
        """
        :param integer frameId: Retrieve the scopes for this stackframe.
        """
        self.frameId = frameId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'frameId': self.frameId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('scopes')
@register
class ScopesResponse(BaseSchema):
    """
    Response to 'scopes' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "scopes": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Scope"
                    },
                    "description": "The scopes of the stackframe. If the array has length zero, there are no scopes available."
                }
            },
            "required": [
                "scopes"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param ScopesResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = ScopesResponseBody()
        else:
            self.body = ScopesResponseBody(**body) if body.__class__ !=  ScopesResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('variables')
@register
class VariablesRequest(BaseSchema):
    """
    Retrieves all child variables for the given variable reference.
    
    An optional filter can be used to limit the fetched children to either named or indexed children.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "variables"
            ]
        },
        "arguments": {
            "type": "VariablesArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param VariablesArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'variables'
        if arguments is None:
            self.arguments = VariablesArguments()
        else:
            self.arguments = VariablesArguments(**arguments) if arguments.__class__ !=  VariablesArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class VariablesArguments(BaseSchema):
    """
    Arguments for 'variables' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "variablesReference": {
            "type": "integer",
            "description": "The Variable reference."
        },
        "filter": {
            "type": "string",
            "enum": [
                "indexed",
                "named"
            ],
            "description": "Optional filter to limit the child variables to either named or indexed. If omitted, both types are fetched."
        },
        "start": {
            "type": "integer",
            "description": "The index of the first variable to return; if omitted children start at 0."
        },
        "count": {
            "type": "integer",
            "description": "The number of variables to return. If count is missing or 0, all variables are returned."
        },
        "format": {
            "description": "Specifies details on how to format the Variable values.\nThe attribute is only honored by a debug adapter if the capability 'supportsValueFormattingOptions' is true.",
            "type": "ValueFormat"
        }
    }
    __refs__ = {'format'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, variablesReference, filter=None, start=None, count=None, format=None, **kwargs):
        """
        :param integer variablesReference: The Variable reference.
        :param string filter: Optional filter to limit the child variables to either named or indexed. If omitted, both types are fetched.
        :param integer start: The index of the first variable to return; if omitted children start at 0.
        :param integer count: The number of variables to return. If count is missing or 0, all variables are returned.
        :param ValueFormat format: Specifies details on how to format the Variable values.
        The attribute is only honored by a debug adapter if the capability 'supportsValueFormattingOptions' is true.
        """
        self.variablesReference = variablesReference
        self.filter = filter
        self.start = start
        self.count = count
        if format is None:
            self.format = ValueFormat()
        else:
            self.format = ValueFormat(**format) if format.__class__ !=  ValueFormat else format
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'variablesReference': self.variablesReference,
        }
        if self.filter is not None:
            dct['filter'] = self.filter
        if self.start is not None:
            dct['start'] = self.start
        if self.count is not None:
            dct['count'] = self.count
        if self.format is not None:
            dct['format'] = self.format.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('variables')
@register
class VariablesResponse(BaseSchema):
    """
    Response to 'variables' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "variables": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Variable"
                    },
                    "description": "All (or a range) of variables for the given variable reference."
                }
            },
            "required": [
                "variables"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param VariablesResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = VariablesResponseBody()
        else:
            self.body = VariablesResponseBody(**body) if body.__class__ !=  VariablesResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setVariable')
@register
class SetVariableRequest(BaseSchema):
    """
    Set the variable with the given name in the variable container to a new value. Clients should only
    call this request if the capability 'supportsSetVariable' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setVariable"
            ]
        },
        "arguments": {
            "type": "SetVariableArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetVariableArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setVariable'
        if arguments is None:
            self.arguments = SetVariableArguments()
        else:
            self.arguments = SetVariableArguments(**arguments) if arguments.__class__ !=  SetVariableArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetVariableArguments(BaseSchema):
    """
    Arguments for 'setVariable' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "variablesReference": {
            "type": "integer",
            "description": "The reference of the variable container."
        },
        "name": {
            "type": "string",
            "description": "The name of the variable in the container."
        },
        "value": {
            "type": "string",
            "description": "The value of the variable."
        },
        "format": {
            "description": "Specifies details on how to format the response value.",
            "type": "ValueFormat"
        }
    }
    __refs__ = {'format'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, variablesReference, name, value, format=None, **kwargs):
        """
        :param integer variablesReference: The reference of the variable container.
        :param string name: The name of the variable in the container.
        :param string value: The value of the variable.
        :param ValueFormat format: Specifies details on how to format the response value.
        """
        self.variablesReference = variablesReference
        self.name = name
        self.value = value
        if format is None:
            self.format = ValueFormat()
        else:
            self.format = ValueFormat(**format) if format.__class__ !=  ValueFormat else format
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'variablesReference': self.variablesReference,
             'name': self.name,
             'value': self.value,
        }
        if self.format is not None:
            dct['format'] = self.format.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('setVariable')
@register
class SetVariableResponse(BaseSchema):
    """
    Response to 'setVariable' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "The new value of the variable."
                },
                "type": {
                    "type": "string",
                    "description": "The type of the new value. Typically shown in the UI when hovering over the value."
                },
                "variablesReference": {
                    "type": "integer",
                    "description": "If variablesReference is > 0, the new value is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "namedVariables": {
                    "type": "integer",
                    "description": "The number of named child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "indexedVariables": {
                    "type": "integer",
                    "description": "The number of indexed child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                }
            },
            "required": [
                "value"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SetVariableResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SetVariableResponseBody()
        else:
            self.body = SetVariableResponseBody(**body) if body.__class__ !=  SetVariableResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('source')
@register
class SourceRequest(BaseSchema):
    """
    The request retrieves the source code for a given source reference.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "source"
            ]
        },
        "arguments": {
            "type": "SourceArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SourceArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'source'
        if arguments is None:
            self.arguments = SourceArguments()
        else:
            self.arguments = SourceArguments(**arguments) if arguments.__class__ !=  SourceArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SourceArguments(BaseSchema):
    """
    Arguments for 'source' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "source": {
            "description": "Specifies the source content to load. Either source.path or source.sourceReference must be specified.",
            "type": "Source"
        },
        "sourceReference": {
            "type": "integer",
            "description": "The reference to the source. This is the same as source.sourceReference.\nThis is provided for backward compatibility since old backends do not understand the 'source' attribute."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, sourceReference, source=None, **kwargs):
        """
        :param integer sourceReference: The reference to the source. This is the same as source.sourceReference.
        This is provided for backward compatibility since old backends do not understand the 'source' attribute.
        :param Source source: Specifies the source content to load. Either source.path or source.sourceReference must be specified.
        """
        self.sourceReference = sourceReference
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'sourceReference': self.sourceReference,
        }
        if self.source is not None:
            dct['source'] = self.source.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('source')
@register
class SourceResponse(BaseSchema):
    """
    Response to 'source' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "Content of the source reference."
                },
                "mimeType": {
                    "type": "string",
                    "description": "Optional content type (mime type) of the source."
                }
            },
            "required": [
                "content"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SourceResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SourceResponseBody()
        else:
            self.body = SourceResponseBody(**body) if body.__class__ !=  SourceResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('threads')
@register
class ThreadsRequest(BaseSchema):
    """
    The request retrieves a list of all threads.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "threads"
            ]
        },
        "arguments": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Object containing arguments for the command."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] arguments: Object containing arguments for the command.
        """
        self.type = 'request'
        self.command = 'threads'
        self.seq = seq
        self.arguments = arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments
        dct.update(self.kwargs)
        return dct


@register_response('threads')
@register
class ThreadsResponse(BaseSchema):
    """
    Response to 'threads' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "threads": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Thread"
                    },
                    "description": "All threads."
                }
            },
            "required": [
                "threads"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param ThreadsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = ThreadsResponseBody()
        else:
            self.body = ThreadsResponseBody(**body) if body.__class__ !=  ThreadsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('terminateThreads')
@register
class TerminateThreadsRequest(BaseSchema):
    """
    The request terminates the threads with the given ids.
    
    Clients should only call this request if the capability 'supportsTerminateThreadsRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "terminateThreads"
            ]
        },
        "arguments": {
            "type": "TerminateThreadsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param TerminateThreadsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'terminateThreads'
        if arguments is None:
            self.arguments = TerminateThreadsArguments()
        else:
            self.arguments = TerminateThreadsArguments(**arguments) if arguments.__class__ !=  TerminateThreadsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class TerminateThreadsArguments(BaseSchema):
    """
    Arguments for 'terminateThreads' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadIds": {
            "type": "array",
            "items": {
                "type": "integer"
            },
            "description": "Ids of threads to be terminated."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadIds=None, **kwargs):
        """
        :param array threadIds: Ids of threads to be terminated.
        """
        self.threadIds = threadIds
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.threadIds is not None:
            dct['threadIds'] = self.threadIds
        dct.update(self.kwargs)
        return dct


@register_response('terminateThreads')
@register
class TerminateThreadsResponse(BaseSchema):
    """
    Response to 'terminateThreads' request. This is just an acknowledgement, so no body field is
    required.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Contains request result if success is true and optional error details if success is false."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] body: Contains request result if success is true and optional error details if success is false.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        self.body = body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body
        dct.update(self.kwargs)
        return dct


@register_request('modules')
@register
class ModulesRequest(BaseSchema):
    """
    Modules can be retrieved from the debug adapter with this request which can either return all
    modules or a range of modules to support paging.
    
    Clients should only call this request if the capability 'supportsModulesRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "modules"
            ]
        },
        "arguments": {
            "type": "ModulesArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param ModulesArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'modules'
        if arguments is None:
            self.arguments = ModulesArguments()
        else:
            self.arguments = ModulesArguments(**arguments) if arguments.__class__ !=  ModulesArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ModulesArguments(BaseSchema):
    """
    Arguments for 'modules' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "startModule": {
            "type": "integer",
            "description": "The index of the first module to return; if omitted modules start at 0."
        },
        "moduleCount": {
            "type": "integer",
            "description": "The number of modules to return. If moduleCount is not specified or 0, all modules are returned."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, startModule=None, moduleCount=None, **kwargs):
        """
        :param integer startModule: The index of the first module to return; if omitted modules start at 0.
        :param integer moduleCount: The number of modules to return. If moduleCount is not specified or 0, all modules are returned.
        """
        self.startModule = startModule
        self.moduleCount = moduleCount
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.startModule is not None:
            dct['startModule'] = self.startModule
        if self.moduleCount is not None:
            dct['moduleCount'] = self.moduleCount
        dct.update(self.kwargs)
        return dct


@register_response('modules')
@register
class ModulesResponse(BaseSchema):
    """
    Response to 'modules' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "modules": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Module"
                    },
                    "description": "All modules or range of modules."
                },
                "totalModules": {
                    "type": "integer",
                    "description": "The total number of modules available."
                }
            },
            "required": [
                "modules"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param ModulesResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = ModulesResponseBody()
        else:
            self.body = ModulesResponseBody(**body) if body.__class__ !=  ModulesResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('loadedSources')
@register
class LoadedSourcesRequest(BaseSchema):
    """
    Retrieves the set of all sources currently loaded by the debugged process.
    
    Clients should only call this request if the capability 'supportsLoadedSourcesRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "loadedSources"
            ]
        },
        "arguments": {
            "type": "LoadedSourcesArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, seq=-1, arguments=None, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param LoadedSourcesArguments arguments: 
        """
        self.type = 'request'
        self.command = 'loadedSources'
        self.seq = seq
        if arguments is None:
            self.arguments = LoadedSourcesArguments()
        else:
            self.arguments = LoadedSourcesArguments(**arguments) if arguments.__class__ !=  LoadedSourcesArguments else arguments
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'seq': self.seq,
        }
        if self.arguments is not None:
            dct['arguments'] = self.arguments.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class LoadedSourcesArguments(BaseSchema):
    """
    Arguments for 'loadedSources' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register_response('loadedSources')
@register
class LoadedSourcesResponse(BaseSchema):
    """
    Response to 'loadedSources' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "sources": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Source"
                    },
                    "description": "Set of loaded sources."
                }
            },
            "required": [
                "sources"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param LoadedSourcesResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = LoadedSourcesResponseBody()
        else:
            self.body = LoadedSourcesResponseBody(**body) if body.__class__ !=  LoadedSourcesResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('evaluate')
@register
class EvaluateRequest(BaseSchema):
    """
    Evaluates the given expression in the context of the top most stack frame.
    
    The expression has access to any variables and arguments that are in scope.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "evaluate"
            ]
        },
        "arguments": {
            "type": "EvaluateArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param EvaluateArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'evaluate'
        if arguments is None:
            self.arguments = EvaluateArguments()
        else:
            self.arguments = EvaluateArguments(**arguments) if arguments.__class__ !=  EvaluateArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class EvaluateArguments(BaseSchema):
    """
    Arguments for 'evaluate' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "expression": {
            "type": "string",
            "description": "The expression to evaluate."
        },
        "frameId": {
            "type": "integer",
            "description": "Evaluate the expression in the scope of this stack frame. If not specified, the expression is evaluated in the global scope."
        },
        "context": {
            "type": "string",
            "_enum": [
                "watch",
                "repl",
                "hover",
                "clipboard"
            ],
            "enumDescriptions": [
                "evaluate is run in a watch.",
                "evaluate is run from REPL console.",
                "evaluate is run from a data hover.",
                "evaluate is run to generate the value that will be stored in the clipboard.\nThe attribute is only honored by a debug adapter if the capability 'supportsClipboardContext' is true."
            ],
            "description": "The context in which the evaluate request is run."
        },
        "format": {
            "description": "Specifies details on how to format the Evaluate result.\nThe attribute is only honored by a debug adapter if the capability 'supportsValueFormattingOptions' is true.",
            "type": "ValueFormat"
        }
    }
    __refs__ = {'format'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, expression, frameId=None, context=None, format=None, **kwargs):
        """
        :param string expression: The expression to evaluate.
        :param integer frameId: Evaluate the expression in the scope of this stack frame. If not specified, the expression is evaluated in the global scope.
        :param string context: The context in which the evaluate request is run.
        :param ValueFormat format: Specifies details on how to format the Evaluate result.
        The attribute is only honored by a debug adapter if the capability 'supportsValueFormattingOptions' is true.
        """
        self.expression = expression
        self.frameId = frameId
        self.context = context
        if format is None:
            self.format = ValueFormat()
        else:
            self.format = ValueFormat(**format) if format.__class__ !=  ValueFormat else format
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'expression': self.expression,
        }
        if self.frameId is not None:
            dct['frameId'] = self.frameId
        if self.context is not None:
            dct['context'] = self.context
        if self.format is not None:
            dct['format'] = self.format.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('evaluate')
@register
class EvaluateResponse(BaseSchema):
    """
    Response to 'evaluate' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "result": {
                    "type": "string",
                    "description": "The result of the evaluate request."
                },
                "type": {
                    "type": "string",
                    "description": "The optional type of the evaluate result.\nThis attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request."
                },
                "presentationHint": {
                    "$ref": "#/definitions/VariablePresentationHint",
                    "description": "Properties of a evaluate result that can be used to determine how to render the result in the UI."
                },
                "variablesReference": {
                    "type": "integer",
                    "description": "If variablesReference is > 0, the evaluate result is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "namedVariables": {
                    "type": "integer",
                    "description": "The number of named child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "indexedVariables": {
                    "type": "integer",
                    "description": "The number of indexed child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "memoryReference": {
                    "type": "string",
                    "description": "Optional memory reference to a location appropriate for this result.\nFor pointer type eval results, this is generally a reference to the memory address contained in the pointer.\nThis attribute should be returned by a debug adapter if the client has passed the value true for the 'supportsMemoryReferences' capability of the 'initialize' request."
                }
            },
            "required": [
                "result",
                "variablesReference"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param EvaluateResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = EvaluateResponseBody()
        else:
            self.body = EvaluateResponseBody(**body) if body.__class__ !=  EvaluateResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('setExpression')
@register
class SetExpressionRequest(BaseSchema):
    """
    Evaluates the given 'value' expression and assigns it to the 'expression' which must be a modifiable
    l-value.
    
    The expressions have access to any variables and arguments that are in scope of the specified frame.
    
    Clients should only call this request if the capability 'supportsSetExpression' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "setExpression"
            ]
        },
        "arguments": {
            "type": "SetExpressionArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param SetExpressionArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'setExpression'
        if arguments is None:
            self.arguments = SetExpressionArguments()
        else:
            self.arguments = SetExpressionArguments(**arguments) if arguments.__class__ !=  SetExpressionArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetExpressionArguments(BaseSchema):
    """
    Arguments for 'setExpression' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "expression": {
            "type": "string",
            "description": "The l-value expression to assign to."
        },
        "value": {
            "type": "string",
            "description": "The value expression to assign to the l-value expression."
        },
        "frameId": {
            "type": "integer",
            "description": "Evaluate the expressions in the scope of this stack frame. If not specified, the expressions are evaluated in the global scope."
        },
        "format": {
            "description": "Specifies how the resulting value should be formatted.",
            "type": "ValueFormat"
        }
    }
    __refs__ = {'format'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, expression, value, frameId=None, format=None, **kwargs):
        """
        :param string expression: The l-value expression to assign to.
        :param string value: The value expression to assign to the l-value expression.
        :param integer frameId: Evaluate the expressions in the scope of this stack frame. If not specified, the expressions are evaluated in the global scope.
        :param ValueFormat format: Specifies how the resulting value should be formatted.
        """
        self.expression = expression
        self.value = value
        self.frameId = frameId
        if format is None:
            self.format = ValueFormat()
        else:
            self.format = ValueFormat(**format) if format.__class__ !=  ValueFormat else format
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'expression': self.expression,
             'value': self.value,
        }
        if self.frameId is not None:
            dct['frameId'] = self.frameId
        if self.format is not None:
            dct['format'] = self.format.to_dict()
        dct.update(self.kwargs)
        return dct


@register_response('setExpression')
@register
class SetExpressionResponse(BaseSchema):
    """
    Response to 'setExpression' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "The new value of the expression."
                },
                "type": {
                    "type": "string",
                    "description": "The optional type of the value.\nThis attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request."
                },
                "presentationHint": {
                    "$ref": "#/definitions/VariablePresentationHint",
                    "description": "Properties of a value that can be used to determine how to render the result in the UI."
                },
                "variablesReference": {
                    "type": "integer",
                    "description": "If variablesReference is > 0, the value is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "namedVariables": {
                    "type": "integer",
                    "description": "The number of named child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                },
                "indexedVariables": {
                    "type": "integer",
                    "description": "The number of indexed child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
                }
            },
            "required": [
                "value"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param SetExpressionResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = SetExpressionResponseBody()
        else:
            self.body = SetExpressionResponseBody(**body) if body.__class__ !=  SetExpressionResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('stepInTargets')
@register
class StepInTargetsRequest(BaseSchema):
    """
    This request retrieves the possible stepIn targets for the specified stack frame.
    
    These targets can be used in the 'stepIn' request.
    
    The StepInTargets may only be called if the 'supportsStepInTargetsRequest' capability exists and is
    true.
    
    Clients should only call this request if the capability 'supportsStepInTargetsRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "stepInTargets"
            ]
        },
        "arguments": {
            "type": "StepInTargetsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param StepInTargetsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'stepInTargets'
        if arguments is None:
            self.arguments = StepInTargetsArguments()
        else:
            self.arguments = StepInTargetsArguments(**arguments) if arguments.__class__ !=  StepInTargetsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class StepInTargetsArguments(BaseSchema):
    """
    Arguments for 'stepInTargets' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "frameId": {
            "type": "integer",
            "description": "The stack frame for which to retrieve the possible stepIn targets."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, frameId, **kwargs):
        """
        :param integer frameId: The stack frame for which to retrieve the possible stepIn targets.
        """
        self.frameId = frameId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'frameId': self.frameId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('stepInTargets')
@register
class StepInTargetsResponse(BaseSchema):
    """
    Response to 'stepInTargets' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "targets": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/StepInTarget"
                    },
                    "description": "The possible stepIn targets of the specified source location."
                }
            },
            "required": [
                "targets"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param StepInTargetsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = StepInTargetsResponseBody()
        else:
            self.body = StepInTargetsResponseBody(**body) if body.__class__ !=  StepInTargetsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('gotoTargets')
@register
class GotoTargetsRequest(BaseSchema):
    """
    This request retrieves the possible goto targets for the specified source location.
    
    These targets can be used in the 'goto' request.
    
    Clients should only call this request if the capability 'supportsGotoTargetsRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "gotoTargets"
            ]
        },
        "arguments": {
            "type": "GotoTargetsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param GotoTargetsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'gotoTargets'
        if arguments is None:
            self.arguments = GotoTargetsArguments()
        else:
            self.arguments = GotoTargetsArguments(**arguments) if arguments.__class__ !=  GotoTargetsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class GotoTargetsArguments(BaseSchema):
    """
    Arguments for 'gotoTargets' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "source": {
            "description": "The source location for which the goto targets are determined.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "The line location for which the goto targets are determined."
        },
        "column": {
            "type": "integer",
            "description": "An optional column location for which the goto targets are determined."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, source, line, column=None, **kwargs):
        """
        :param Source source: The source location for which the goto targets are determined.
        :param integer line: The line location for which the goto targets are determined.
        :param integer column: An optional column location for which the goto targets are determined.
        """
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.line = line
        self.column = column
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'source': self.source.to_dict(),
             'line': self.line,
        }
        if self.column is not None:
            dct['column'] = self.column
        dct.update(self.kwargs)
        return dct


@register_response('gotoTargets')
@register
class GotoTargetsResponse(BaseSchema):
    """
    Response to 'gotoTargets' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "targets": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/GotoTarget"
                    },
                    "description": "The possible goto targets of the specified location."
                }
            },
            "required": [
                "targets"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param GotoTargetsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = GotoTargetsResponseBody()
        else:
            self.body = GotoTargetsResponseBody(**body) if body.__class__ !=  GotoTargetsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('completions')
@register
class CompletionsRequest(BaseSchema):
    """
    Returns a list of possible completions for a given caret position and text.
    
    Clients should only call this request if the capability 'supportsCompletionsRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "completions"
            ]
        },
        "arguments": {
            "type": "CompletionsArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param CompletionsArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'completions'
        if arguments is None:
            self.arguments = CompletionsArguments()
        else:
            self.arguments = CompletionsArguments(**arguments) if arguments.__class__ !=  CompletionsArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class CompletionsArguments(BaseSchema):
    """
    Arguments for 'completions' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "frameId": {
            "type": "integer",
            "description": "Returns completions in the scope of this stack frame. If not specified, the completions are returned for the global scope."
        },
        "text": {
            "type": "string",
            "description": "One or more source lines. Typically this is the text a user has typed into the debug console before he asked for completion."
        },
        "column": {
            "type": "integer",
            "description": "The character position for which to determine the completion proposals."
        },
        "line": {
            "type": "integer",
            "description": "An optional line for which to determine the completion proposals. If missing the first line of the text is assumed."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, text, column, frameId=None, line=None, **kwargs):
        """
        :param string text: One or more source lines. Typically this is the text a user has typed into the debug console before he asked for completion.
        :param integer column: The character position for which to determine the completion proposals.
        :param integer frameId: Returns completions in the scope of this stack frame. If not specified, the completions are returned for the global scope.
        :param integer line: An optional line for which to determine the completion proposals. If missing the first line of the text is assumed.
        """
        self.text = text
        self.column = column
        self.frameId = frameId
        self.line = line
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'text': self.text,
             'column': self.column,
        }
        if self.frameId is not None:
            dct['frameId'] = self.frameId
        if self.line is not None:
            dct['line'] = self.line
        dct.update(self.kwargs)
        return dct


@register_response('completions')
@register
class CompletionsResponse(BaseSchema):
    """
    Response to 'completions' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "targets": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/CompletionItem"
                    },
                    "description": "The possible completions for ."
                }
            },
            "required": [
                "targets"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param CompletionsResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = CompletionsResponseBody()
        else:
            self.body = CompletionsResponseBody(**body) if body.__class__ !=  CompletionsResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('exceptionInfo')
@register
class ExceptionInfoRequest(BaseSchema):
    """
    Retrieves the details of the exception that caused this event to be raised.
    
    Clients should only call this request if the capability 'supportsExceptionInfoRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "exceptionInfo"
            ]
        },
        "arguments": {
            "type": "ExceptionInfoArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param ExceptionInfoArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'exceptionInfo'
        if arguments is None:
            self.arguments = ExceptionInfoArguments()
        else:
            self.arguments = ExceptionInfoArguments(**arguments) if arguments.__class__ !=  ExceptionInfoArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ExceptionInfoArguments(BaseSchema):
    """
    Arguments for 'exceptionInfo' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "Thread for which exception information should be retrieved."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, **kwargs):
        """
        :param integer threadId: Thread for which exception information should be retrieved.
        """
        self.threadId = threadId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        dct.update(self.kwargs)
        return dct


@register_response('exceptionInfo')
@register
class ExceptionInfoResponse(BaseSchema):
    """
    Response to 'exceptionInfo' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "exceptionId": {
                    "type": "string",
                    "description": "ID of the exception that was thrown."
                },
                "description": {
                    "type": "string",
                    "description": "Descriptive text for the exception provided by the debug adapter."
                },
                "breakMode": {
                    "$ref": "#/definitions/ExceptionBreakMode",
                    "description": "Mode that caused the exception notification to be raised."
                },
                "details": {
                    "$ref": "#/definitions/ExceptionDetails",
                    "description": "Detailed information about the exception."
                }
            },
            "required": [
                "exceptionId",
                "breakMode"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, body, seq=-1, message=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param ExceptionInfoResponseBody body: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        if body is None:
            self.body = ExceptionInfoResponseBody()
        else:
            self.body = ExceptionInfoResponseBody(**body) if body.__class__ !=  ExceptionInfoResponseBody else body
        self.seq = seq
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'body': self.body.to_dict(),
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register_request('readMemory')
@register
class ReadMemoryRequest(BaseSchema):
    """
    Reads bytes from memory at the provided location.
    
    Clients should only call this request if the capability 'supportsReadMemoryRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "readMemory"
            ]
        },
        "arguments": {
            "type": "ReadMemoryArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param ReadMemoryArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'readMemory'
        if arguments is None:
            self.arguments = ReadMemoryArguments()
        else:
            self.arguments = ReadMemoryArguments(**arguments) if arguments.__class__ !=  ReadMemoryArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class ReadMemoryArguments(BaseSchema):
    """
    Arguments for 'readMemory' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "memoryReference": {
            "type": "string",
            "description": "Memory reference to the base location from which data should be read."
        },
        "offset": {
            "type": "integer",
            "description": "Optional offset (in bytes) to be applied to the reference location before reading data. Can be negative."
        },
        "count": {
            "type": "integer",
            "description": "Number of bytes to read at the specified location and offset."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, memoryReference, count, offset=None, **kwargs):
        """
        :param string memoryReference: Memory reference to the base location from which data should be read.
        :param integer count: Number of bytes to read at the specified location and offset.
        :param integer offset: Optional offset (in bytes) to be applied to the reference location before reading data. Can be negative.
        """
        self.memoryReference = memoryReference
        self.count = count
        self.offset = offset
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'memoryReference': self.memoryReference,
             'count': self.count,
        }
        if self.offset is not None:
            dct['offset'] = self.offset
        dct.update(self.kwargs)
        return dct


@register_response('readMemory')
@register
class ReadMemoryResponse(BaseSchema):
    """
    Response to 'readMemory' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string",
                    "description": "The address of the first byte of data returned.\nTreated as a hex value if prefixed with '0x', or as a decimal value otherwise."
                },
                "unreadableBytes": {
                    "type": "integer",
                    "description": "The number of unreadable bytes encountered after the last successfully read byte.\nThis can be used to determine the number of bytes that must be skipped before a subsequent 'readMemory' request will succeed."
                },
                "data": {
                    "type": "string",
                    "description": "The bytes read from memory, encoded using base64."
                }
            },
            "required": [
                "address"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param ReadMemoryResponseBody body: 
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        if body is None:
            self.body = ReadMemoryResponseBody()
        else:
            self.body = ReadMemoryResponseBody(**body) if body.__class__ !=  ReadMemoryResponseBody else body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body.to_dict()
        dct.update(self.kwargs)
        return dct


@register_request('disassemble')
@register
class DisassembleRequest(BaseSchema):
    """
    Disassembles code stored at the provided location.
    
    Clients should only call this request if the capability 'supportsDisassembleRequest' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "request"
            ]
        },
        "command": {
            "type": "string",
            "enum": [
                "disassemble"
            ]
        },
        "arguments": {
            "type": "DisassembleArguments"
        }
    }
    __refs__ = {'arguments'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, arguments, seq=-1, **kwargs):
        """
        :param string type: 
        :param string command: 
        :param DisassembleArguments arguments: 
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        """
        self.type = 'request'
        self.command = 'disassemble'
        if arguments is None:
            self.arguments = DisassembleArguments()
        else:
            self.arguments = DisassembleArguments(**arguments) if arguments.__class__ !=  DisassembleArguments else arguments
        self.seq = seq
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'command': self.command,
             'arguments': self.arguments.to_dict(),
             'seq': self.seq,
        }
        dct.update(self.kwargs)
        return dct


@register
class DisassembleArguments(BaseSchema):
    """
    Arguments for 'disassemble' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "memoryReference": {
            "type": "string",
            "description": "Memory reference to the base location containing the instructions to disassemble."
        },
        "offset": {
            "type": "integer",
            "description": "Optional offset (in bytes) to be applied to the reference location before disassembling. Can be negative."
        },
        "instructionOffset": {
            "type": "integer",
            "description": "Optional offset (in instructions) to be applied after the byte offset (if any) before disassembling. Can be negative."
        },
        "instructionCount": {
            "type": "integer",
            "description": "Number of instructions to disassemble starting at the specified location and offset.\nAn adapter must return exactly this number of instructions - any unavailable instructions should be replaced with an implementation-defined 'invalid instruction' value."
        },
        "resolveSymbols": {
            "type": "boolean",
            "description": "If true, the adapter should attempt to resolve memory addresses and other values to symbolic names."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, memoryReference, instructionCount, offset=None, instructionOffset=None, resolveSymbols=None, **kwargs):
        """
        :param string memoryReference: Memory reference to the base location containing the instructions to disassemble.
        :param integer instructionCount: Number of instructions to disassemble starting at the specified location and offset.
        An adapter must return exactly this number of instructions - any unavailable instructions should be replaced with an implementation-defined 'invalid instruction' value.
        :param integer offset: Optional offset (in bytes) to be applied to the reference location before disassembling. Can be negative.
        :param integer instructionOffset: Optional offset (in instructions) to be applied after the byte offset (if any) before disassembling. Can be negative.
        :param boolean resolveSymbols: If true, the adapter should attempt to resolve memory addresses and other values to symbolic names.
        """
        self.memoryReference = memoryReference
        self.instructionCount = instructionCount
        self.offset = offset
        self.instructionOffset = instructionOffset
        self.resolveSymbols = resolveSymbols
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'memoryReference': self.memoryReference,
             'instructionCount': self.instructionCount,
        }
        if self.offset is not None:
            dct['offset'] = self.offset
        if self.instructionOffset is not None:
            dct['instructionOffset'] = self.instructionOffset
        if self.resolveSymbols is not None:
            dct['resolveSymbols'] = self.resolveSymbols
        dct.update(self.kwargs)
        return dct


@register_response('disassemble')
@register
class DisassembleResponse(BaseSchema):
    """
    Response to 'disassemble' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "seq": {
            "type": "integer",
            "description": "Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request."
        },
        "type": {
            "type": "string",
            "enum": [
                "response"
            ]
        },
        "request_seq": {
            "type": "integer",
            "description": "Sequence number of the corresponding request."
        },
        "success": {
            "type": "boolean",
            "description": "Outcome of the request.\nIf true, the request was successful and the 'body' attribute may contain the result of the request.\nIf the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error')."
        },
        "command": {
            "type": "string",
            "description": "The command requested."
        },
        "message": {
            "type": "string",
            "description": "Contains the raw error in short form if 'success' is false.\nThis raw error might be interpreted by the frontend and is not shown in the UI.\nSome predefined values exist.",
            "_enum": [
                "cancelled"
            ],
            "enumDescriptions": [
                "request was cancelled."
            ]
        },
        "body": {
            "type": "object",
            "properties": {
                "instructions": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/DisassembledInstruction"
                    },
                    "description": "The list of disassembled instructions."
                }
            },
            "required": [
                "instructions"
            ]
        }
    }
    __refs__ = {'body'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, request_seq, success, command, seq=-1, message=None, body=None, **kwargs):
        """
        :param string type: 
        :param integer request_seq: Sequence number of the corresponding request.
        :param boolean success: Outcome of the request.
        If true, the request was successful and the 'body' attribute may contain the result of the request.
        If the value is false, the attribute 'message' contains the error in short form and the 'body' may contain additional information (see 'ErrorResponse.body.error').
        :param string command: The command requested.
        :param integer seq: Sequence number (also known as message ID). For protocol messages of type 'request' this ID can be used to cancel the request.
        :param string message: Contains the raw error in short form if 'success' is false.
        This raw error might be interpreted by the frontend and is not shown in the UI.
        Some predefined values exist.
        :param DisassembleResponseBody body: 
        """
        self.type = 'response'
        self.request_seq = request_seq
        self.success = success
        self.command = command
        self.seq = seq
        self.message = message
        if body is None:
            self.body = DisassembleResponseBody()
        else:
            self.body = DisassembleResponseBody(**body) if body.__class__ !=  DisassembleResponseBody else body
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'type': self.type,
             'request_seq': self.request_seq,
             'success': self.success,
             'command': self.command,
             'seq': self.seq,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.body is not None:
            dct['body'] = self.body.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class Capabilities(BaseSchema):
    """
    Information about the capabilities of a debug adapter.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "supportsConfigurationDoneRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'configurationDone' request."
        },
        "supportsFunctionBreakpoints": {
            "type": "boolean",
            "description": "The debug adapter supports function breakpoints."
        },
        "supportsConditionalBreakpoints": {
            "type": "boolean",
            "description": "The debug adapter supports conditional breakpoints."
        },
        "supportsHitConditionalBreakpoints": {
            "type": "boolean",
            "description": "The debug adapter supports breakpoints that break execution after a specified number of hits."
        },
        "supportsEvaluateForHovers": {
            "type": "boolean",
            "description": "The debug adapter supports a (side effect free) evaluate request for data hovers."
        },
        "exceptionBreakpointFilters": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ExceptionBreakpointsFilter"
            },
            "description": "Available filters or options for the setExceptionBreakpoints request."
        },
        "supportsStepBack": {
            "type": "boolean",
            "description": "The debug adapter supports stepping back via the 'stepBack' and 'reverseContinue' requests."
        },
        "supportsSetVariable": {
            "type": "boolean",
            "description": "The debug adapter supports setting a variable to a value."
        },
        "supportsRestartFrame": {
            "type": "boolean",
            "description": "The debug adapter supports restarting a frame."
        },
        "supportsGotoTargetsRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'gotoTargets' request."
        },
        "supportsStepInTargetsRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'stepInTargets' request."
        },
        "supportsCompletionsRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'completions' request."
        },
        "completionTriggerCharacters": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "The set of characters that should trigger completion in a REPL. If not specified, the UI should assume the '.' character."
        },
        "supportsModulesRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'modules' request."
        },
        "additionalModuleColumns": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ColumnDescriptor"
            },
            "description": "The set of additional module information exposed by the debug adapter."
        },
        "supportedChecksumAlgorithms": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ChecksumAlgorithm"
            },
            "description": "Checksum algorithms supported by the debug adapter."
        },
        "supportsRestartRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'restart' request. In this case a client should not implement 'restart' by terminating and relaunching the adapter but by calling the RestartRequest."
        },
        "supportsExceptionOptions": {
            "type": "boolean",
            "description": "The debug adapter supports 'exceptionOptions' on the setExceptionBreakpoints request."
        },
        "supportsValueFormattingOptions": {
            "type": "boolean",
            "description": "The debug adapter supports a 'format' attribute on the stackTraceRequest, variablesRequest, and evaluateRequest."
        },
        "supportsExceptionInfoRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'exceptionInfo' request."
        },
        "supportTerminateDebuggee": {
            "type": "boolean",
            "description": "The debug adapter supports the 'terminateDebuggee' attribute on the 'disconnect' request."
        },
        "supportsDelayedStackTraceLoading": {
            "type": "boolean",
            "description": "The debug adapter supports the delayed loading of parts of the stack, which requires that both the 'startFrame' and 'levels' arguments and the 'totalFrames' result of the 'StackTrace' request are supported."
        },
        "supportsLoadedSourcesRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'loadedSources' request."
        },
        "supportsLogPoints": {
            "type": "boolean",
            "description": "The debug adapter supports logpoints by interpreting the 'logMessage' attribute of the SourceBreakpoint."
        },
        "supportsTerminateThreadsRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'terminateThreads' request."
        },
        "supportsSetExpression": {
            "type": "boolean",
            "description": "The debug adapter supports the 'setExpression' request."
        },
        "supportsTerminateRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'terminate' request."
        },
        "supportsDataBreakpoints": {
            "type": "boolean",
            "description": "The debug adapter supports data breakpoints."
        },
        "supportsReadMemoryRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'readMemory' request."
        },
        "supportsDisassembleRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'disassemble' request."
        },
        "supportsCancelRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'cancel' request."
        },
        "supportsBreakpointLocationsRequest": {
            "type": "boolean",
            "description": "The debug adapter supports the 'breakpointLocations' request."
        },
        "supportsClipboardContext": {
            "type": "boolean",
            "description": "The debug adapter supports the 'clipboard' context value in the 'evaluate' request."
        },
        "supportsSteppingGranularity": {
            "type": "boolean",
            "description": "The debug adapter supports stepping granularities (argument 'granularity') for the stepping requests."
        },
        "supportsInstructionBreakpoints": {
            "type": "boolean",
            "description": "The debug adapter supports adding breakpoints based on instruction references."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, supportsConfigurationDoneRequest=None, supportsFunctionBreakpoints=None, supportsConditionalBreakpoints=None, supportsHitConditionalBreakpoints=None, supportsEvaluateForHovers=None, exceptionBreakpointFilters=None, supportsStepBack=None, supportsSetVariable=None, supportsRestartFrame=None, supportsGotoTargetsRequest=None, supportsStepInTargetsRequest=None, supportsCompletionsRequest=None, completionTriggerCharacters=None, supportsModulesRequest=None, additionalModuleColumns=None, supportedChecksumAlgorithms=None, supportsRestartRequest=None, supportsExceptionOptions=None, supportsValueFormattingOptions=None, supportsExceptionInfoRequest=None, supportTerminateDebuggee=None, supportsDelayedStackTraceLoading=None, supportsLoadedSourcesRequest=None, supportsLogPoints=None, supportsTerminateThreadsRequest=None, supportsSetExpression=None, supportsTerminateRequest=None, supportsDataBreakpoints=None, supportsReadMemoryRequest=None, supportsDisassembleRequest=None, supportsCancelRequest=None, supportsBreakpointLocationsRequest=None, supportsClipboardContext=None, supportsSteppingGranularity=None, supportsInstructionBreakpoints=None, **kwargs):
        """
        :param boolean supportsConfigurationDoneRequest: The debug adapter supports the 'configurationDone' request.
        :param boolean supportsFunctionBreakpoints: The debug adapter supports function breakpoints.
        :param boolean supportsConditionalBreakpoints: The debug adapter supports conditional breakpoints.
        :param boolean supportsHitConditionalBreakpoints: The debug adapter supports breakpoints that break execution after a specified number of hits.
        :param boolean supportsEvaluateForHovers: The debug adapter supports a (side effect free) evaluate request for data hovers.
        :param array exceptionBreakpointFilters: Available filters or options for the setExceptionBreakpoints request.
        :param boolean supportsStepBack: The debug adapter supports stepping back via the 'stepBack' and 'reverseContinue' requests.
        :param boolean supportsSetVariable: The debug adapter supports setting a variable to a value.
        :param boolean supportsRestartFrame: The debug adapter supports restarting a frame.
        :param boolean supportsGotoTargetsRequest: The debug adapter supports the 'gotoTargets' request.
        :param boolean supportsStepInTargetsRequest: The debug adapter supports the 'stepInTargets' request.
        :param boolean supportsCompletionsRequest: The debug adapter supports the 'completions' request.
        :param array completionTriggerCharacters: The set of characters that should trigger completion in a REPL. If not specified, the UI should assume the '.' character.
        :param boolean supportsModulesRequest: The debug adapter supports the 'modules' request.
        :param array additionalModuleColumns: The set of additional module information exposed by the debug adapter.
        :param array supportedChecksumAlgorithms: Checksum algorithms supported by the debug adapter.
        :param boolean supportsRestartRequest: The debug adapter supports the 'restart' request. In this case a client should not implement 'restart' by terminating and relaunching the adapter but by calling the RestartRequest.
        :param boolean supportsExceptionOptions: The debug adapter supports 'exceptionOptions' on the setExceptionBreakpoints request.
        :param boolean supportsValueFormattingOptions: The debug adapter supports a 'format' attribute on the stackTraceRequest, variablesRequest, and evaluateRequest.
        :param boolean supportsExceptionInfoRequest: The debug adapter supports the 'exceptionInfo' request.
        :param boolean supportTerminateDebuggee: The debug adapter supports the 'terminateDebuggee' attribute on the 'disconnect' request.
        :param boolean supportsDelayedStackTraceLoading: The debug adapter supports the delayed loading of parts of the stack, which requires that both the 'startFrame' and 'levels' arguments and the 'totalFrames' result of the 'StackTrace' request are supported.
        :param boolean supportsLoadedSourcesRequest: The debug adapter supports the 'loadedSources' request.
        :param boolean supportsLogPoints: The debug adapter supports logpoints by interpreting the 'logMessage' attribute of the SourceBreakpoint.
        :param boolean supportsTerminateThreadsRequest: The debug adapter supports the 'terminateThreads' request.
        :param boolean supportsSetExpression: The debug adapter supports the 'setExpression' request.
        :param boolean supportsTerminateRequest: The debug adapter supports the 'terminate' request.
        :param boolean supportsDataBreakpoints: The debug adapter supports data breakpoints.
        :param boolean supportsReadMemoryRequest: The debug adapter supports the 'readMemory' request.
        :param boolean supportsDisassembleRequest: The debug adapter supports the 'disassemble' request.
        :param boolean supportsCancelRequest: The debug adapter supports the 'cancel' request.
        :param boolean supportsBreakpointLocationsRequest: The debug adapter supports the 'breakpointLocations' request.
        :param boolean supportsClipboardContext: The debug adapter supports the 'clipboard' context value in the 'evaluate' request.
        :param boolean supportsSteppingGranularity: The debug adapter supports stepping granularities (argument 'granularity') for the stepping requests.
        :param boolean supportsInstructionBreakpoints: The debug adapter supports adding breakpoints based on instruction references.
        """
        self.supportsConfigurationDoneRequest = supportsConfigurationDoneRequest
        self.supportsFunctionBreakpoints = supportsFunctionBreakpoints
        self.supportsConditionalBreakpoints = supportsConditionalBreakpoints
        self.supportsHitConditionalBreakpoints = supportsHitConditionalBreakpoints
        self.supportsEvaluateForHovers = supportsEvaluateForHovers
        self.exceptionBreakpointFilters = exceptionBreakpointFilters
        self.supportsStepBack = supportsStepBack
        self.supportsSetVariable = supportsSetVariable
        self.supportsRestartFrame = supportsRestartFrame
        self.supportsGotoTargetsRequest = supportsGotoTargetsRequest
        self.supportsStepInTargetsRequest = supportsStepInTargetsRequest
        self.supportsCompletionsRequest = supportsCompletionsRequest
        self.completionTriggerCharacters = completionTriggerCharacters
        self.supportsModulesRequest = supportsModulesRequest
        self.additionalModuleColumns = additionalModuleColumns
        self.supportedChecksumAlgorithms = supportedChecksumAlgorithms
        self.supportsRestartRequest = supportsRestartRequest
        self.supportsExceptionOptions = supportsExceptionOptions
        self.supportsValueFormattingOptions = supportsValueFormattingOptions
        self.supportsExceptionInfoRequest = supportsExceptionInfoRequest
        self.supportTerminateDebuggee = supportTerminateDebuggee
        self.supportsDelayedStackTraceLoading = supportsDelayedStackTraceLoading
        self.supportsLoadedSourcesRequest = supportsLoadedSourcesRequest
        self.supportsLogPoints = supportsLogPoints
        self.supportsTerminateThreadsRequest = supportsTerminateThreadsRequest
        self.supportsSetExpression = supportsSetExpression
        self.supportsTerminateRequest = supportsTerminateRequest
        self.supportsDataBreakpoints = supportsDataBreakpoints
        self.supportsReadMemoryRequest = supportsReadMemoryRequest
        self.supportsDisassembleRequest = supportsDisassembleRequest
        self.supportsCancelRequest = supportsCancelRequest
        self.supportsBreakpointLocationsRequest = supportsBreakpointLocationsRequest
        self.supportsClipboardContext = supportsClipboardContext
        self.supportsSteppingGranularity = supportsSteppingGranularity
        self.supportsInstructionBreakpoints = supportsInstructionBreakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.supportsConfigurationDoneRequest is not None:
            dct['supportsConfigurationDoneRequest'] = self.supportsConfigurationDoneRequest
        if self.supportsFunctionBreakpoints is not None:
            dct['supportsFunctionBreakpoints'] = self.supportsFunctionBreakpoints
        if self.supportsConditionalBreakpoints is not None:
            dct['supportsConditionalBreakpoints'] = self.supportsConditionalBreakpoints
        if self.supportsHitConditionalBreakpoints is not None:
            dct['supportsHitConditionalBreakpoints'] = self.supportsHitConditionalBreakpoints
        if self.supportsEvaluateForHovers is not None:
            dct['supportsEvaluateForHovers'] = self.supportsEvaluateForHovers
        if self.exceptionBreakpointFilters is not None:
            dct['exceptionBreakpointFilters'] = self.exceptionBreakpointFilters
        if self.supportsStepBack is not None:
            dct['supportsStepBack'] = self.supportsStepBack
        if self.supportsSetVariable is not None:
            dct['supportsSetVariable'] = self.supportsSetVariable
        if self.supportsRestartFrame is not None:
            dct['supportsRestartFrame'] = self.supportsRestartFrame
        if self.supportsGotoTargetsRequest is not None:
            dct['supportsGotoTargetsRequest'] = self.supportsGotoTargetsRequest
        if self.supportsStepInTargetsRequest is not None:
            dct['supportsStepInTargetsRequest'] = self.supportsStepInTargetsRequest
        if self.supportsCompletionsRequest is not None:
            dct['supportsCompletionsRequest'] = self.supportsCompletionsRequest
        if self.completionTriggerCharacters is not None:
            dct['completionTriggerCharacters'] = self.completionTriggerCharacters
        if self.supportsModulesRequest is not None:
            dct['supportsModulesRequest'] = self.supportsModulesRequest
        if self.additionalModuleColumns is not None:
            dct['additionalModuleColumns'] = self.additionalModuleColumns
        if self.supportedChecksumAlgorithms is not None:
            dct['supportedChecksumAlgorithms'] = self.supportedChecksumAlgorithms
        if self.supportsRestartRequest is not None:
            dct['supportsRestartRequest'] = self.supportsRestartRequest
        if self.supportsExceptionOptions is not None:
            dct['supportsExceptionOptions'] = self.supportsExceptionOptions
        if self.supportsValueFormattingOptions is not None:
            dct['supportsValueFormattingOptions'] = self.supportsValueFormattingOptions
        if self.supportsExceptionInfoRequest is not None:
            dct['supportsExceptionInfoRequest'] = self.supportsExceptionInfoRequest
        if self.supportTerminateDebuggee is not None:
            dct['supportTerminateDebuggee'] = self.supportTerminateDebuggee
        if self.supportsDelayedStackTraceLoading is not None:
            dct['supportsDelayedStackTraceLoading'] = self.supportsDelayedStackTraceLoading
        if self.supportsLoadedSourcesRequest is not None:
            dct['supportsLoadedSourcesRequest'] = self.supportsLoadedSourcesRequest
        if self.supportsLogPoints is not None:
            dct['supportsLogPoints'] = self.supportsLogPoints
        if self.supportsTerminateThreadsRequest is not None:
            dct['supportsTerminateThreadsRequest'] = self.supportsTerminateThreadsRequest
        if self.supportsSetExpression is not None:
            dct['supportsSetExpression'] = self.supportsSetExpression
        if self.supportsTerminateRequest is not None:
            dct['supportsTerminateRequest'] = self.supportsTerminateRequest
        if self.supportsDataBreakpoints is not None:
            dct['supportsDataBreakpoints'] = self.supportsDataBreakpoints
        if self.supportsReadMemoryRequest is not None:
            dct['supportsReadMemoryRequest'] = self.supportsReadMemoryRequest
        if self.supportsDisassembleRequest is not None:
            dct['supportsDisassembleRequest'] = self.supportsDisassembleRequest
        if self.supportsCancelRequest is not None:
            dct['supportsCancelRequest'] = self.supportsCancelRequest
        if self.supportsBreakpointLocationsRequest is not None:
            dct['supportsBreakpointLocationsRequest'] = self.supportsBreakpointLocationsRequest
        if self.supportsClipboardContext is not None:
            dct['supportsClipboardContext'] = self.supportsClipboardContext
        if self.supportsSteppingGranularity is not None:
            dct['supportsSteppingGranularity'] = self.supportsSteppingGranularity
        if self.supportsInstructionBreakpoints is not None:
            dct['supportsInstructionBreakpoints'] = self.supportsInstructionBreakpoints
        dct.update(self.kwargs)
        return dct


@register
class ExceptionBreakpointsFilter(BaseSchema):
    """
    An ExceptionBreakpointsFilter is shown in the UI as an option for configuring how exceptions are
    dealt with.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "filter": {
            "type": "string",
            "description": "The internal ID of the filter. This value is passed to the setExceptionBreakpoints request."
        },
        "label": {
            "type": "string",
            "description": "The name of the filter. This will be shown in the UI."
        },
        "default": {
            "type": "boolean",
            "description": "Initial value of the filter. If not specified a value 'false' is assumed."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, filter, label, default=None, **kwargs):
        """
        :param string filter: The internal ID of the filter. This value is passed to the setExceptionBreakpoints request.
        :param string label: The name of the filter. This will be shown in the UI.
        :param boolean default: Initial value of the filter. If not specified a value 'false' is assumed.
        """
        self.filter = filter
        self.label = label
        self.default = default
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'filter': self.filter,
             'label': self.label,
        }
        if self.default is not None:
            dct['default'] = self.default
        dct.update(self.kwargs)
        return dct


@register
class Message(BaseSchema):
    """
    A structured message object. Used to return errors from requests.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": "integer",
            "description": "Unique identifier for the message."
        },
        "format": {
            "type": "string",
            "description": "A format string for the message. Embedded variables have the form '{name}'.\nIf variable name starts with an underscore character, the variable does not contain user data (PII) and can be safely used for telemetry purposes."
        },
        "variables": {
            "type": "object",
            "description": "An object used as a dictionary for looking up the variables in the format string.",
            "additionalProperties": {
                "type": "string",
                "description": "Values must be strings."
            }
        },
        "sendTelemetry": {
            "type": "boolean",
            "description": "If true send to telemetry."
        },
        "showUser": {
            "type": "boolean",
            "description": "If true show user."
        },
        "url": {
            "type": "string",
            "description": "An optional url where additional information about this message can be found."
        },
        "urlLabel": {
            "type": "string",
            "description": "An optional label that is presented to the user as the UI for opening the url."
        }
    }
    __refs__ = {'variables'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, id, format, variables=None, sendTelemetry=None, showUser=None, url=None, urlLabel=None, **kwargs):
        """
        :param integer id: Unique identifier for the message.
        :param string format: A format string for the message. Embedded variables have the form '{name}'.
        If variable name starts with an underscore character, the variable does not contain user data (PII) and can be safely used for telemetry purposes.
        :param MessageVariables variables: An object used as a dictionary for looking up the variables in the format string.
        :param boolean sendTelemetry: If true send to telemetry.
        :param boolean showUser: If true show user.
        :param string url: An optional url where additional information about this message can be found.
        :param string urlLabel: An optional label that is presented to the user as the UI for opening the url.
        """
        self.id = id
        self.format = format
        if variables is None:
            self.variables = MessageVariables()
        else:
            self.variables = MessageVariables(**variables) if variables.__class__ !=  MessageVariables else variables
        self.sendTelemetry = sendTelemetry
        self.showUser = showUser
        self.url = url
        self.urlLabel = urlLabel
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'id': self.id,
             'format': self.format,
        }
        if self.variables is not None:
            dct['variables'] = self.variables.to_dict()
        if self.sendTelemetry is not None:
            dct['sendTelemetry'] = self.sendTelemetry
        if self.showUser is not None:
            dct['showUser'] = self.showUser
        if self.url is not None:
            dct['url'] = self.url
        if self.urlLabel is not None:
            dct['urlLabel'] = self.urlLabel
        dct.update(self.kwargs)
        return dct


@register
class Module(BaseSchema):
    """
    A Module object represents a row in the modules view.
    
    Two attributes are mandatory: an id identifies a module in the modules view and is used in a
    ModuleEvent for identifying a module for adding, updating or deleting.
    
    The name is used to minimally render the module in the UI.
    
    
    Additional attributes can be added to the module. They will show up in the module View if they have
    a corresponding ColumnDescriptor.
    
    
    To avoid an unnecessary proliferation of additional attributes with similar semantics but different
    names
    
    we recommend to re-use attributes from the 'recommended' list below first, and only introduce new
    attributes if nothing appropriate could be found.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": [
                "integer",
                "string"
            ],
            "description": "Unique identifier for the module."
        },
        "name": {
            "type": "string",
            "description": "A name of the module."
        },
        "path": {
            "type": "string",
            "description": "optional but recommended attributes.\nalways try to use these first before introducing additional attributes.\n\nLogical full path to the module. The exact definition is implementation defined, but usually this would be a full path to the on-disk file for the module."
        },
        "isOptimized": {
            "type": "boolean",
            "description": "True if the module is optimized."
        },
        "isUserCode": {
            "type": "boolean",
            "description": "True if the module is considered 'user code' by a debugger that supports 'Just My Code'."
        },
        "version": {
            "type": "string",
            "description": "Version of Module."
        },
        "symbolStatus": {
            "type": "string",
            "description": "User understandable description of if symbols were found for the module (ex: 'Symbols Loaded', 'Symbols not found', etc."
        },
        "symbolFilePath": {
            "type": "string",
            "description": "Logical full path to the symbol file. The exact definition is implementation defined."
        },
        "dateTimeStamp": {
            "type": "string",
            "description": "Module created or modified."
        },
        "addressRange": {
            "type": "string",
            "description": "Address range covered by this module."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, id, name, path=None, isOptimized=None, isUserCode=None, version=None, symbolStatus=None, symbolFilePath=None, dateTimeStamp=None, addressRange=None, **kwargs):
        """
        :param ['integer', 'string'] id: Unique identifier for the module.
        :param string name: A name of the module.
        :param string path: optional but recommended attributes.
        always try to use these first before introducing additional attributes.
        
        Logical full path to the module. The exact definition is implementation defined, but usually this would be a full path to the on-disk file for the module.
        :param boolean isOptimized: True if the module is optimized.
        :param boolean isUserCode: True if the module is considered 'user code' by a debugger that supports 'Just My Code'.
        :param string version: Version of Module.
        :param string symbolStatus: User understandable description of if symbols were found for the module (ex: 'Symbols Loaded', 'Symbols not found', etc.
        :param string symbolFilePath: Logical full path to the symbol file. The exact definition is implementation defined.
        :param string dateTimeStamp: Module created or modified.
        :param string addressRange: Address range covered by this module.
        """
        self.id = id
        self.name = name
        self.path = path
        self.isOptimized = isOptimized
        self.isUserCode = isUserCode
        self.version = version
        self.symbolStatus = symbolStatus
        self.symbolFilePath = symbolFilePath
        self.dateTimeStamp = dateTimeStamp
        self.addressRange = addressRange
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'id': self.id,
             'name': self.name,
        }
        if self.path is not None:
            dct['path'] = self.path
        if self.isOptimized is not None:
            dct['isOptimized'] = self.isOptimized
        if self.isUserCode is not None:
            dct['isUserCode'] = self.isUserCode
        if self.version is not None:
            dct['version'] = self.version
        if self.symbolStatus is not None:
            dct['symbolStatus'] = self.symbolStatus
        if self.symbolFilePath is not None:
            dct['symbolFilePath'] = self.symbolFilePath
        if self.dateTimeStamp is not None:
            dct['dateTimeStamp'] = self.dateTimeStamp
        if self.addressRange is not None:
            dct['addressRange'] = self.addressRange
        dct.update(self.kwargs)
        return dct


@register
class ColumnDescriptor(BaseSchema):
    """
    A ColumnDescriptor specifies what module attribute to show in a column of the ModulesView, how to
    format it,
    
    and what the column's label should be.
    
    It is only used if the underlying UI actually supports this level of customization.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "attributeName": {
            "type": "string",
            "description": "Name of the attribute rendered in this column."
        },
        "label": {
            "type": "string",
            "description": "Header UI label of column."
        },
        "format": {
            "type": "string",
            "description": "Format to use for the rendered values in this column. TBD how the format strings looks like."
        },
        "type": {
            "type": "string",
            "enum": [
                "string",
                "number",
                "boolean",
                "unixTimestampUTC"
            ],
            "description": "Datatype of values in this column.  Defaults to 'string' if not specified."
        },
        "width": {
            "type": "integer",
            "description": "Width of this column in characters (hint only)."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, attributeName, label, format=None, type=None, width=None, **kwargs):
        """
        :param string attributeName: Name of the attribute rendered in this column.
        :param string label: Header UI label of column.
        :param string format: Format to use for the rendered values in this column. TBD how the format strings looks like.
        :param string type: Datatype of values in this column.  Defaults to 'string' if not specified.
        :param integer width: Width of this column in characters (hint only).
        """
        self.attributeName = attributeName
        self.label = label
        self.format = format
        self.type = type
        self.width = width
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'attributeName': self.attributeName,
             'label': self.label,
        }
        if self.format is not None:
            dct['format'] = self.format
        if self.type is not None:
            dct['type'] = self.type
        if self.width is not None:
            dct['width'] = self.width
        dct.update(self.kwargs)
        return dct


@register
class ModulesViewDescriptor(BaseSchema):
    """
    The ModulesViewDescriptor is the container for all declarative configuration options of a
    ModuleView.
    
    For now it only specifies the columns to be shown in the modules view.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "columns": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ColumnDescriptor"
            }
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, columns, **kwargs):
        """
        :param array columns: 
        """
        self.columns = columns
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'columns': self.columns,
        }
        dct.update(self.kwargs)
        return dct


@register
class Thread(BaseSchema):
    """
    A Thread

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": "integer",
            "description": "Unique identifier for the thread."
        },
        "name": {
            "type": "string",
            "description": "A name of the thread."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, id, name, **kwargs):
        """
        :param integer id: Unique identifier for the thread.
        :param string name: A name of the thread.
        """
        self.id = id
        self.name = name
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'id': self.id,
             'name': self.name,
        }
        dct.update(self.kwargs)
        return dct


@register
class Source(BaseSchema):
    """
    A Source is a descriptor for source code.
    
    It is returned from the debug adapter as part of a StackFrame and it is used by clients when
    specifying breakpoints.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "name": {
            "type": "string",
            "description": "The short name of the source. Every source returned from the debug adapter has a name.\nWhen sending a source to the debug adapter this name is optional."
        },
        "path": {
            "type": "string",
            "description": "The path of the source to be shown in the UI.\nIt is only used to locate and load the content of the source if no sourceReference is specified (or its value is 0)."
        },
        "sourceReference": {
            "type": "integer",
            "description": "If sourceReference > 0 the contents of the source must be retrieved through the SourceRequest (even if a path is specified).\nA sourceReference is only valid for a session, so it must not be used to persist a source.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "presentationHint": {
            "type": "string",
            "description": "An optional hint for how to present the source in the UI.\nA value of 'deemphasize' can be used to indicate that the source is not available or that it is skipped on stepping.",
            "enum": [
                "normal",
                "emphasize",
                "deemphasize"
            ]
        },
        "origin": {
            "type": "string",
            "description": "The (optional) origin of this source: possible values 'internal module', 'inlined content from source map', etc."
        },
        "sources": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Source"
            },
            "description": "An optional list of sources that are related to this source. These may be the source that generated this source."
        },
        "adapterData": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Optional data that a debug adapter might want to loop through the client.\nThe client should leave the data intact and persist it across sessions. The client should not interpret the data."
        },
        "checksums": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Checksum"
            },
            "description": "The checksums associated with this file."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, name=None, path=None, sourceReference=None, presentationHint=None, origin=None, sources=None, adapterData=None, checksums=None, **kwargs):
        """
        :param string name: The short name of the source. Every source returned from the debug adapter has a name.
        When sending a source to the debug adapter this name is optional.
        :param string path: The path of the source to be shown in the UI.
        It is only used to locate and load the content of the source if no sourceReference is specified (or its value is 0).
        :param integer sourceReference: If sourceReference > 0 the contents of the source must be retrieved through the SourceRequest (even if a path is specified).
        A sourceReference is only valid for a session, so it must not be used to persist a source.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param string presentationHint: An optional hint for how to present the source in the UI.
        A value of 'deemphasize' can be used to indicate that the source is not available or that it is skipped on stepping.
        :param string origin: The (optional) origin of this source: possible values 'internal module', 'inlined content from source map', etc.
        :param array sources: An optional list of sources that are related to this source. These may be the source that generated this source.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] adapterData: Optional data that a debug adapter might want to loop through the client.
        The client should leave the data intact and persist it across sessions. The client should not interpret the data.
        :param array checksums: The checksums associated with this file.
        """
        self.name = name
        self.path = path
        self.sourceReference = sourceReference
        self.presentationHint = presentationHint
        self.origin = origin
        self.sources = sources
        self.adapterData = adapterData
        self.checksums = checksums
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.name is not None:
            dct['name'] = self.name
        if self.path is not None:
            dct['path'] = self.path
        if self.sourceReference is not None:
            dct['sourceReference'] = self.sourceReference
        if self.presentationHint is not None:
            dct['presentationHint'] = self.presentationHint
        if self.origin is not None:
            dct['origin'] = self.origin
        if self.sources is not None:
            dct['sources'] = self.sources
        if self.adapterData is not None:
            dct['adapterData'] = self.adapterData
        if self.checksums is not None:
            dct['checksums'] = self.checksums
        dct.update(self.kwargs)
        return dct


@register
class StackFrame(BaseSchema):
    """
    A Stackframe contains the source location.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": "integer",
            "description": "An identifier for the stack frame. It must be unique across all threads.\nThis id can be used to retrieve the scopes of the frame with the 'scopesRequest' or to restart the execution of a stackframe."
        },
        "name": {
            "type": "string",
            "description": "The name of the stack frame, typically a method name."
        },
        "source": {
            "description": "The optional source of the frame.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "The line within the file of the frame. If source is null or doesn't exist, line is 0 and must be ignored."
        },
        "column": {
            "type": "integer",
            "description": "The column within the line. If source is null or doesn't exist, column is 0 and must be ignored."
        },
        "endLine": {
            "type": "integer",
            "description": "An optional end line of the range covered by the stack frame."
        },
        "endColumn": {
            "type": "integer",
            "description": "An optional end column of the range covered by the stack frame."
        },
        "instructionPointerReference": {
            "type": "string",
            "description": "Optional memory reference for the current instruction pointer in this frame."
        },
        "moduleId": {
            "type": [
                "integer",
                "string"
            ],
            "description": "The module associated with this frame, if any."
        },
        "presentationHint": {
            "type": "string",
            "enum": [
                "normal",
                "label",
                "subtle"
            ],
            "description": "An optional hint for how to present this frame in the UI.\nA value of 'label' can be used to indicate that the frame is an artificial frame that is used as a visual label or separator. A value of 'subtle' can be used to change the appearance of a frame in a 'subtle' way."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, id, name, line, column, source=None, endLine=None, endColumn=None, instructionPointerReference=None, moduleId=None, presentationHint=None, **kwargs):
        """
        :param integer id: An identifier for the stack frame. It must be unique across all threads.
        This id can be used to retrieve the scopes of the frame with the 'scopesRequest' or to restart the execution of a stackframe.
        :param string name: The name of the stack frame, typically a method name.
        :param integer line: The line within the file of the frame. If source is null or doesn't exist, line is 0 and must be ignored.
        :param integer column: The column within the line. If source is null or doesn't exist, column is 0 and must be ignored.
        :param Source source: The optional source of the frame.
        :param integer endLine: An optional end line of the range covered by the stack frame.
        :param integer endColumn: An optional end column of the range covered by the stack frame.
        :param string instructionPointerReference: Optional memory reference for the current instruction pointer in this frame.
        :param ['integer', 'string'] moduleId: The module associated with this frame, if any.
        :param string presentationHint: An optional hint for how to present this frame in the UI.
        A value of 'label' can be used to indicate that the frame is an artificial frame that is used as a visual label or separator. A value of 'subtle' can be used to change the appearance of a frame in a 'subtle' way.
        """
        self.id = id
        self.name = name
        self.line = line
        self.column = column
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.endLine = endLine
        self.endColumn = endColumn
        self.instructionPointerReference = instructionPointerReference
        self.moduleId = moduleId
        self.presentationHint = presentationHint
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'id': self.id,
             'name': self.name,
             'line': self.line,
             'column': self.column,
        }
        if self.source is not None:
            dct['source'] = self.source.to_dict()
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        if self.instructionPointerReference is not None:
            dct['instructionPointerReference'] = self.instructionPointerReference
        if self.moduleId is not None:
            dct['moduleId'] = self.moduleId
        if self.presentationHint is not None:
            dct['presentationHint'] = self.presentationHint
        dct.update(self.kwargs)
        return dct


@register
class Scope(BaseSchema):
    """
    A Scope is a named container for variables. Optionally a scope can map to a source or a range within
    a source.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "name": {
            "type": "string",
            "description": "Name of the scope such as 'Arguments', 'Locals', or 'Registers'. This string is shown in the UI as is and can be translated."
        },
        "presentationHint": {
            "type": "string",
            "description": "An optional hint for how to present this scope in the UI. If this attribute is missing, the scope is shown with a generic UI.",
            "_enum": [
                "arguments",
                "locals",
                "registers"
            ],
            "enumDescriptions": [
                "Scope contains method arguments.",
                "Scope contains local variables.",
                "Scope contains registers. Only a single 'registers' scope should be returned from a 'scopes' request."
            ]
        },
        "variablesReference": {
            "type": "integer",
            "description": "The variables of this scope can be retrieved by passing the value of variablesReference to the VariablesRequest."
        },
        "namedVariables": {
            "type": "integer",
            "description": "The number of named variables in this scope.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks."
        },
        "indexedVariables": {
            "type": "integer",
            "description": "The number of indexed variables in this scope.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks."
        },
        "expensive": {
            "type": "boolean",
            "description": "If true, the number of variables in this scope is large or expensive to retrieve."
        },
        "source": {
            "description": "Optional source for this scope.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "Optional start line of the range covered by this scope."
        },
        "column": {
            "type": "integer",
            "description": "Optional start column of the range covered by this scope."
        },
        "endLine": {
            "type": "integer",
            "description": "Optional end line of the range covered by this scope."
        },
        "endColumn": {
            "type": "integer",
            "description": "Optional end column of the range covered by this scope."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, name, variablesReference, expensive, presentationHint=None, namedVariables=None, indexedVariables=None, source=None, line=None, column=None, endLine=None, endColumn=None, **kwargs):
        """
        :param string name: Name of the scope such as 'Arguments', 'Locals', or 'Registers'. This string is shown in the UI as is and can be translated.
        :param integer variablesReference: The variables of this scope can be retrieved by passing the value of variablesReference to the VariablesRequest.
        :param boolean expensive: If true, the number of variables in this scope is large or expensive to retrieve.
        :param string presentationHint: An optional hint for how to present this scope in the UI. If this attribute is missing, the scope is shown with a generic UI.
        :param integer namedVariables: The number of named variables in this scope.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        :param integer indexedVariables: The number of indexed variables in this scope.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        :param Source source: Optional source for this scope.
        :param integer line: Optional start line of the range covered by this scope.
        :param integer column: Optional start column of the range covered by this scope.
        :param integer endLine: Optional end line of the range covered by this scope.
        :param integer endColumn: Optional end column of the range covered by this scope.
        """
        self.name = name
        self.variablesReference = variablesReference
        self.expensive = expensive
        self.presentationHint = presentationHint
        self.namedVariables = namedVariables
        self.indexedVariables = indexedVariables
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'name': self.name,
             'variablesReference': self.variablesReference,
             'expensive': self.expensive,
        }
        if self.presentationHint is not None:
            dct['presentationHint'] = self.presentationHint
        if self.namedVariables is not None:
            dct['namedVariables'] = self.namedVariables
        if self.indexedVariables is not None:
            dct['indexedVariables'] = self.indexedVariables
        if self.source is not None:
            dct['source'] = self.source.to_dict()
        if self.line is not None:
            dct['line'] = self.line
        if self.column is not None:
            dct['column'] = self.column
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        dct.update(self.kwargs)
        return dct


@register
class Variable(BaseSchema):
    """
    A Variable is a name/value pair.
    
    Optionally a variable can have a 'type' that is shown if space permits or when hovering over the
    variable's name.
    
    An optional 'kind' is used to render additional properties of the variable, e.g. different icons can
    be used to indicate that a variable is public or private.
    
    If the value is structured (has children), a handle is provided to retrieve the children with the
    VariablesRequest.
    
    If the number of named or indexed children is large, the numbers should be returned via the optional
    'namedVariables' and 'indexedVariables' attributes.
    
    The client can use this optional information to present the children in a paged UI and fetch them in
    chunks.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "name": {
            "type": "string",
            "description": "The variable's name."
        },
        "value": {
            "type": "string",
            "description": "The variable's value. This can be a multi-line text, e.g. for a function the body of a function."
        },
        "type": {
            "type": "string",
            "description": "The type of the variable's value. Typically shown in the UI when hovering over the value.\nThis attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request."
        },
        "presentationHint": {
            "description": "Properties of a variable that can be used to determine how to render the variable in the UI.",
            "type": "VariablePresentationHint"
        },
        "evaluateName": {
            "type": "string",
            "description": "Optional evaluatable name of this variable which can be passed to the 'EvaluateRequest' to fetch the variable's value."
        },
        "variablesReference": {
            "type": "integer",
            "description": "If variablesReference is > 0, the variable is structured and its children can be retrieved by passing variablesReference to the VariablesRequest."
        },
        "namedVariables": {
            "type": "integer",
            "description": "The number of named child variables.\nThe client can use this optional information to present the children in a paged UI and fetch them in chunks."
        },
        "indexedVariables": {
            "type": "integer",
            "description": "The number of indexed child variables.\nThe client can use this optional information to present the children in a paged UI and fetch them in chunks."
        },
        "memoryReference": {
            "type": "string",
            "description": "Optional memory reference for the variable if the variable represents executable code, such as a function pointer.\nThis attribute is only required if the client has passed the value true for the 'supportsMemoryReferences' capability of the 'initialize' request."
        }
    }
    __refs__ = {'presentationHint'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, name, value, variablesReference, type=None, presentationHint=None, evaluateName=None, namedVariables=None, indexedVariables=None, memoryReference=None, **kwargs):
        """
        :param string name: The variable's name.
        :param string value: The variable's value. This can be a multi-line text, e.g. for a function the body of a function.
        :param integer variablesReference: If variablesReference is > 0, the variable is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.
        :param string type: The type of the variable's value. Typically shown in the UI when hovering over the value.
        This attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request.
        :param VariablePresentationHint presentationHint: Properties of a variable that can be used to determine how to render the variable in the UI.
        :param string evaluateName: Optional evaluatable name of this variable which can be passed to the 'EvaluateRequest' to fetch the variable's value.
        :param integer namedVariables: The number of named child variables.
        The client can use this optional information to present the children in a paged UI and fetch them in chunks.
        :param integer indexedVariables: The number of indexed child variables.
        The client can use this optional information to present the children in a paged UI and fetch them in chunks.
        :param string memoryReference: Optional memory reference for the variable if the variable represents executable code, such as a function pointer.
        This attribute is only required if the client has passed the value true for the 'supportsMemoryReferences' capability of the 'initialize' request.
        """
        self.name = name
        self.value = value
        self.variablesReference = variablesReference
        self.type = type
        if presentationHint is None:
            self.presentationHint = VariablePresentationHint()
        else:
            self.presentationHint = VariablePresentationHint(**presentationHint) if presentationHint.__class__ !=  VariablePresentationHint else presentationHint
        self.evaluateName = evaluateName
        self.namedVariables = namedVariables
        self.indexedVariables = indexedVariables
        self.memoryReference = memoryReference
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'name': self.name,
             'value': self.value,
             'variablesReference': self.variablesReference,
        }
        if self.type is not None:
            dct['type'] = self.type
        if self.presentationHint is not None:
            dct['presentationHint'] = self.presentationHint.to_dict()
        if self.evaluateName is not None:
            dct['evaluateName'] = self.evaluateName
        if self.namedVariables is not None:
            dct['namedVariables'] = self.namedVariables
        if self.indexedVariables is not None:
            dct['indexedVariables'] = self.indexedVariables
        if self.memoryReference is not None:
            dct['memoryReference'] = self.memoryReference
        dct.update(self.kwargs)
        return dct


@register
class VariablePresentationHint(BaseSchema):
    """
    Optional properties of a variable that can be used to determine how to render the variable in the
    UI.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "kind": {
            "description": "The kind of variable. Before introducing additional values, try to use the listed values.",
            "type": "string",
            "_enum": [
                "property",
                "method",
                "class",
                "data",
                "event",
                "baseClass",
                "innerClass",
                "interface",
                "mostDerivedClass",
                "virtual",
                "dataBreakpoint"
            ],
            "enumDescriptions": [
                "Indicates that the object is a property.",
                "Indicates that the object is a method.",
                "Indicates that the object is a class.",
                "Indicates that the object is data.",
                "Indicates that the object is an event.",
                "Indicates that the object is a base class.",
                "Indicates that the object is an inner class.",
                "Indicates that the object is an interface.",
                "Indicates that the object is the most derived class.",
                "Indicates that the object is virtual, that means it is a synthetic object introducedby the\nadapter for rendering purposes, e.g. an index range for large arrays.",
                "Indicates that a data breakpoint is registered for the object."
            ]
        },
        "attributes": {
            "description": "Set of attributes represented as an array of strings. Before introducing additional values, try to use the listed values.",
            "type": "array",
            "items": {
                "type": "string",
                "_enum": [
                    "static",
                    "constant",
                    "readOnly",
                    "rawString",
                    "hasObjectId",
                    "canHaveObjectId",
                    "hasSideEffects"
                ],
                "enumDescriptions": [
                    "Indicates that the object is static.",
                    "Indicates that the object is a constant.",
                    "Indicates that the object is read only.",
                    "Indicates that the object is a raw string.",
                    "Indicates that the object can have an Object ID created for it.",
                    "Indicates that the object has an Object ID associated with it.",
                    "Indicates that the evaluation had side effects."
                ]
            }
        },
        "visibility": {
            "description": "Visibility of variable. Before introducing additional values, try to use the listed values.",
            "type": "string",
            "_enum": [
                "public",
                "private",
                "protected",
                "internal",
                "final"
            ]
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, kind=None, attributes=None, visibility=None, **kwargs):
        """
        :param string kind: The kind of variable. Before introducing additional values, try to use the listed values.
        :param array attributes: Set of attributes represented as an array of strings. Before introducing additional values, try to use the listed values.
        :param string visibility: Visibility of variable. Before introducing additional values, try to use the listed values.
        """
        self.kind = kind
        self.attributes = attributes
        self.visibility = visibility
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.kind is not None:
            dct['kind'] = self.kind
        if self.attributes is not None:
            dct['attributes'] = self.attributes
        if self.visibility is not None:
            dct['visibility'] = self.visibility
        dct.update(self.kwargs)
        return dct


@register
class BreakpointLocation(BaseSchema):
    """
    Properties of a breakpoint location returned from the 'breakpointLocations' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "line": {
            "type": "integer",
            "description": "Start line of breakpoint location."
        },
        "column": {
            "type": "integer",
            "description": "Optional start column of breakpoint location."
        },
        "endLine": {
            "type": "integer",
            "description": "Optional end line of breakpoint location if the location covers a range."
        },
        "endColumn": {
            "type": "integer",
            "description": "Optional end column of breakpoint location if the location covers a range."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, line, column=None, endLine=None, endColumn=None, **kwargs):
        """
        :param integer line: Start line of breakpoint location.
        :param integer column: Optional start column of breakpoint location.
        :param integer endLine: Optional end line of breakpoint location if the location covers a range.
        :param integer endColumn: Optional end column of breakpoint location if the location covers a range.
        """
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'line': self.line,
        }
        if self.column is not None:
            dct['column'] = self.column
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        dct.update(self.kwargs)
        return dct


@register
class SourceBreakpoint(BaseSchema):
    """
    Properties of a breakpoint or logpoint passed to the setBreakpoints request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "line": {
            "type": "integer",
            "description": "The source line of the breakpoint or logpoint."
        },
        "column": {
            "type": "integer",
            "description": "An optional source column of the breakpoint."
        },
        "condition": {
            "type": "string",
            "description": "An optional expression for conditional breakpoints.\nIt is only honored by a debug adapter if the capability 'supportsConditionalBreakpoints' is true."
        },
        "hitCondition": {
            "type": "string",
            "description": "An optional expression that controls how many hits of the breakpoint are ignored.\nThe backend is expected to interpret the expression as needed.\nThe attribute is only honored by a debug adapter if the capability 'supportsHitConditionalBreakpoints' is true."
        },
        "logMessage": {
            "type": "string",
            "description": "If this attribute exists and is non-empty, the backend must not 'break' (stop)\nbut log the message instead. Expressions within {} are interpolated.\nThe attribute is only honored by a debug adapter if the capability 'supportsLogPoints' is true."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, line, column=None, condition=None, hitCondition=None, logMessage=None, **kwargs):
        """
        :param integer line: The source line of the breakpoint or logpoint.
        :param integer column: An optional source column of the breakpoint.
        :param string condition: An optional expression for conditional breakpoints.
        It is only honored by a debug adapter if the capability 'supportsConditionalBreakpoints' is true.
        :param string hitCondition: An optional expression that controls how many hits of the breakpoint are ignored.
        The backend is expected to interpret the expression as needed.
        The attribute is only honored by a debug adapter if the capability 'supportsHitConditionalBreakpoints' is true.
        :param string logMessage: If this attribute exists and is non-empty, the backend must not 'break' (stop)
        but log the message instead. Expressions within {} are interpolated.
        The attribute is only honored by a debug adapter if the capability 'supportsLogPoints' is true.
        """
        self.line = line
        self.column = column
        self.condition = condition
        self.hitCondition = hitCondition
        self.logMessage = logMessage
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'line': self.line,
        }
        if self.column is not None:
            dct['column'] = self.column
        if self.condition is not None:
            dct['condition'] = self.condition
        if self.hitCondition is not None:
            dct['hitCondition'] = self.hitCondition
        if self.logMessage is not None:
            dct['logMessage'] = self.logMessage
        dct.update(self.kwargs)
        return dct


@register
class FunctionBreakpoint(BaseSchema):
    """
    Properties of a breakpoint passed to the setFunctionBreakpoints request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "name": {
            "type": "string",
            "description": "The name of the function."
        },
        "condition": {
            "type": "string",
            "description": "An optional expression for conditional breakpoints.\nIt is only honored by a debug adapter if the capability 'supportsConditionalBreakpoints' is true."
        },
        "hitCondition": {
            "type": "string",
            "description": "An optional expression that controls how many hits of the breakpoint are ignored.\nThe backend is expected to interpret the expression as needed.\nThe attribute is only honored by a debug adapter if the capability 'supportsHitConditionalBreakpoints' is true."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, name, condition=None, hitCondition=None, **kwargs):
        """
        :param string name: The name of the function.
        :param string condition: An optional expression for conditional breakpoints.
        It is only honored by a debug adapter if the capability 'supportsConditionalBreakpoints' is true.
        :param string hitCondition: An optional expression that controls how many hits of the breakpoint are ignored.
        The backend is expected to interpret the expression as needed.
        The attribute is only honored by a debug adapter if the capability 'supportsHitConditionalBreakpoints' is true.
        """
        self.name = name
        self.condition = condition
        self.hitCondition = hitCondition
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'name': self.name,
        }
        if self.condition is not None:
            dct['condition'] = self.condition
        if self.hitCondition is not None:
            dct['hitCondition'] = self.hitCondition
        dct.update(self.kwargs)
        return dct


@register
class DataBreakpointAccessType(BaseSchema):
    """
    This enumeration defines all possible access types for data breakpoints.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class DataBreakpoint(BaseSchema):
    """
    Properties of a data breakpoint passed to the setDataBreakpoints request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "dataId": {
            "type": "string",
            "description": "An id representing the data. This id is returned from the dataBreakpointInfo request."
        },
        "accessType": {
            "description": "The access type of the data.",
            "type": "DataBreakpointAccessType"
        },
        "condition": {
            "type": "string",
            "description": "An optional expression for conditional breakpoints."
        },
        "hitCondition": {
            "type": "string",
            "description": "An optional expression that controls how many hits of the breakpoint are ignored.\nThe backend is expected to interpret the expression as needed."
        }
    }
    __refs__ = {'accessType'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, dataId, accessType=None, condition=None, hitCondition=None, **kwargs):
        """
        :param string dataId: An id representing the data. This id is returned from the dataBreakpointInfo request.
        :param DataBreakpointAccessType accessType: The access type of the data.
        :param string condition: An optional expression for conditional breakpoints.
        :param string hitCondition: An optional expression that controls how many hits of the breakpoint are ignored.
        The backend is expected to interpret the expression as needed.
        """
        self.dataId = dataId
        if accessType is None:
            self.accessType = DataBreakpointAccessType()
        else:
            self.accessType = DataBreakpointAccessType(**accessType) if accessType.__class__ !=  DataBreakpointAccessType else accessType
        self.condition = condition
        self.hitCondition = hitCondition
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'dataId': self.dataId,
        }
        if self.accessType is not None:
            dct['accessType'] = self.accessType.to_dict()
        if self.condition is not None:
            dct['condition'] = self.condition
        if self.hitCondition is not None:
            dct['hitCondition'] = self.hitCondition
        dct.update(self.kwargs)
        return dct


@register
class InstructionBreakpoint(BaseSchema):
    """
    Properties of a breakpoint passed to the setInstructionBreakpoints request

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "instructionReference": {
            "type": "string",
            "description": "The instruction reference of the breakpoint.\nThis should be a memory or instruction pointer reference from an EvaluateResponse, Variable, StackFrame, GotoTarget, or Breakpoint."
        },
        "offset": {
            "type": "integer",
            "description": "An optional offset from the instruction reference.\nThis can be negative."
        },
        "condition": {
            "type": "string",
            "description": "An optional expression for conditional breakpoints.\nIt is only honored by a debug adapter if the capability 'supportsConditionalBreakpoints' is true."
        },
        "hitCondition": {
            "type": "string",
            "description": "An optional expression that controls how many hits of the breakpoint are ignored.\nThe backend is expected to interpret the expression as needed.\nThe attribute is only honored by a debug adapter if the capability 'supportsHitConditionalBreakpoints' is true."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, instructionReference, offset=None, condition=None, hitCondition=None, **kwargs):
        """
        :param string instructionReference: The instruction reference of the breakpoint.
        This should be a memory or instruction pointer reference from an EvaluateResponse, Variable, StackFrame, GotoTarget, or Breakpoint.
        :param integer offset: An optional offset from the instruction reference.
        This can be negative.
        :param string condition: An optional expression for conditional breakpoints.
        It is only honored by a debug adapter if the capability 'supportsConditionalBreakpoints' is true.
        :param string hitCondition: An optional expression that controls how many hits of the breakpoint are ignored.
        The backend is expected to interpret the expression as needed.
        The attribute is only honored by a debug adapter if the capability 'supportsHitConditionalBreakpoints' is true.
        """
        self.instructionReference = instructionReference
        self.offset = offset
        self.condition = condition
        self.hitCondition = hitCondition
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'instructionReference': self.instructionReference,
        }
        if self.offset is not None:
            dct['offset'] = self.offset
        if self.condition is not None:
            dct['condition'] = self.condition
        if self.hitCondition is not None:
            dct['hitCondition'] = self.hitCondition
        dct.update(self.kwargs)
        return dct


@register
class Breakpoint(BaseSchema):
    """
    Information about a Breakpoint created in setBreakpoints, setFunctionBreakpoints,
    setInstructionBreakpoints, or setDataBreakpoints.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": "integer",
            "description": "An optional identifier for the breakpoint. It is needed if breakpoint events are used to update or remove breakpoints."
        },
        "verified": {
            "type": "boolean",
            "description": "If true breakpoint could be set (but not necessarily at the desired location)."
        },
        "message": {
            "type": "string",
            "description": "An optional message about the state of the breakpoint.\nThis is shown to the user and can be used to explain why a breakpoint could not be verified."
        },
        "source": {
            "description": "The source where the breakpoint is located.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "The start line of the actual range covered by the breakpoint."
        },
        "column": {
            "type": "integer",
            "description": "An optional start column of the actual range covered by the breakpoint."
        },
        "endLine": {
            "type": "integer",
            "description": "An optional end line of the actual range covered by the breakpoint."
        },
        "endColumn": {
            "type": "integer",
            "description": "An optional end column of the actual range covered by the breakpoint.\nIf no end line is given, then the end column is assumed to be in the start line."
        },
        "instructionReference": {
            "type": "string",
            "description": "An optional memory reference to where the breakpoint is set."
        },
        "offset": {
            "type": "integer",
            "description": "An optional offset from the instruction reference.\nThis can be negative."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, verified, id=None, message=None, source=None, line=None, column=None, endLine=None, endColumn=None, instructionReference=None, offset=None, **kwargs):
        """
        :param boolean verified: If true breakpoint could be set (but not necessarily at the desired location).
        :param integer id: An optional identifier for the breakpoint. It is needed if breakpoint events are used to update or remove breakpoints.
        :param string message: An optional message about the state of the breakpoint.
        This is shown to the user and can be used to explain why a breakpoint could not be verified.
        :param Source source: The source where the breakpoint is located.
        :param integer line: The start line of the actual range covered by the breakpoint.
        :param integer column: An optional start column of the actual range covered by the breakpoint.
        :param integer endLine: An optional end line of the actual range covered by the breakpoint.
        :param integer endColumn: An optional end column of the actual range covered by the breakpoint.
        If no end line is given, then the end column is assumed to be in the start line.
        :param string instructionReference: An optional memory reference to where the breakpoint is set.
        :param integer offset: An optional offset from the instruction reference.
        This can be negative.
        """
        self.verified = verified
        self.id = id
        self.message = message
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn
        self.instructionReference = instructionReference
        self.offset = offset
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'verified': self.verified,
        }
        if self.id is not None:
            dct['id'] = self.id
        if self.message is not None:
            dct['message'] = self.message
        if self.source is not None:
            dct['source'] = self.source.to_dict()
        if self.line is not None:
            dct['line'] = self.line
        if self.column is not None:
            dct['column'] = self.column
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        if self.instructionReference is not None:
            dct['instructionReference'] = self.instructionReference
        if self.offset is not None:
            dct['offset'] = self.offset
        dct.update(self.kwargs)
        return dct


@register
class SteppingGranularity(BaseSchema):
    """
    The granularity of one 'step' in the stepping requests 'next', 'stepIn', 'stepOut', and 'stepBack'.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class StepInTarget(BaseSchema):
    """
    A StepInTarget can be used in the 'stepIn' request and determines into which single target the
    stepIn request should step.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": "integer",
            "description": "Unique identifier for a stepIn target."
        },
        "label": {
            "type": "string",
            "description": "The name of the stepIn target (shown in the UI)."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, id, label, **kwargs):
        """
        :param integer id: Unique identifier for a stepIn target.
        :param string label: The name of the stepIn target (shown in the UI).
        """
        self.id = id
        self.label = label
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'id': self.id,
             'label': self.label,
        }
        dct.update(self.kwargs)
        return dct


@register
class GotoTarget(BaseSchema):
    """
    A GotoTarget describes a code location that can be used as a target in the 'goto' request.
    
    The possible goto targets can be determined via the 'gotoTargets' request.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "id": {
            "type": "integer",
            "description": "Unique identifier for a goto target. This is used in the goto request."
        },
        "label": {
            "type": "string",
            "description": "The name of the goto target (shown in the UI)."
        },
        "line": {
            "type": "integer",
            "description": "The line of the goto target."
        },
        "column": {
            "type": "integer",
            "description": "An optional column of the goto target."
        },
        "endLine": {
            "type": "integer",
            "description": "An optional end line of the range covered by the goto target."
        },
        "endColumn": {
            "type": "integer",
            "description": "An optional end column of the range covered by the goto target."
        },
        "instructionPointerReference": {
            "type": "string",
            "description": "Optional memory reference for the instruction pointer value represented by this target."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, id, label, line, column=None, endLine=None, endColumn=None, instructionPointerReference=None, **kwargs):
        """
        :param integer id: Unique identifier for a goto target. This is used in the goto request.
        :param string label: The name of the goto target (shown in the UI).
        :param integer line: The line of the goto target.
        :param integer column: An optional column of the goto target.
        :param integer endLine: An optional end line of the range covered by the goto target.
        :param integer endColumn: An optional end column of the range covered by the goto target.
        :param string instructionPointerReference: Optional memory reference for the instruction pointer value represented by this target.
        """
        self.id = id
        self.label = label
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn
        self.instructionPointerReference = instructionPointerReference
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'id': self.id,
             'label': self.label,
             'line': self.line,
        }
        if self.column is not None:
            dct['column'] = self.column
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        if self.instructionPointerReference is not None:
            dct['instructionPointerReference'] = self.instructionPointerReference
        dct.update(self.kwargs)
        return dct


@register
class CompletionItem(BaseSchema):
    """
    CompletionItems are the suggestions returned from the CompletionsRequest.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "label": {
            "type": "string",
            "description": "The label of this completion item. By default this is also the text that is inserted when selecting this completion."
        },
        "text": {
            "type": "string",
            "description": "If text is not falsy then it is inserted instead of the label."
        },
        "sortText": {
            "type": "string",
            "description": "A string that should be used when comparing this item with other items. When `falsy` the label is used."
        },
        "type": {
            "description": "The item's type. Typically the client uses this information to render the item in the UI with an icon.",
            "type": "CompletionItemType"
        },
        "start": {
            "type": "integer",
            "description": "This value determines the location (in the CompletionsRequest's 'text' attribute) where the completion text is added.\nIf missing the text is added at the location specified by the CompletionsRequest's 'column' attribute."
        },
        "length": {
            "type": "integer",
            "description": "This value determines how many characters are overwritten by the completion text.\nIf missing the value 0 is assumed which results in the completion text being inserted."
        },
        "selectionStart": {
            "type": "integer",
            "description": "Determines the start of the new selection after the text has been inserted (or replaced).\nThe start position must in the range 0 and length of the completion text.\nIf omitted the selection starts at the end of the completion text."
        },
        "selectionLength": {
            "type": "integer",
            "description": "Determines the length of the new selection after the text has been inserted (or replaced).\nThe selection can not extend beyond the bounds of the completion text.\nIf omitted the length is assumed to be 0."
        }
    }
    __refs__ = {'type'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, label, text=None, sortText=None, type=None, start=None, length=None, selectionStart=None, selectionLength=None, **kwargs):
        """
        :param string label: The label of this completion item. By default this is also the text that is inserted when selecting this completion.
        :param string text: If text is not falsy then it is inserted instead of the label.
        :param string sortText: A string that should be used when comparing this item with other items. When `falsy` the label is used.
        :param CompletionItemType type: The item's type. Typically the client uses this information to render the item in the UI with an icon.
        :param integer start: This value determines the location (in the CompletionsRequest's 'text' attribute) where the completion text is added.
        If missing the text is added at the location specified by the CompletionsRequest's 'column' attribute.
        :param integer length: This value determines how many characters are overwritten by the completion text.
        If missing the value 0 is assumed which results in the completion text being inserted.
        :param integer selectionStart: Determines the start of the new selection after the text has been inserted (or replaced).
        The start position must in the range 0 and length of the completion text.
        If omitted the selection starts at the end of the completion text.
        :param integer selectionLength: Determines the length of the new selection after the text has been inserted (or replaced).
        The selection can not extend beyond the bounds of the completion text.
        If omitted the length is assumed to be 0.
        """
        self.label = label
        self.text = text
        self.sortText = sortText
        if type is None:
            self.type = CompletionItemType()
        else:
            self.type = CompletionItemType(**type) if type.__class__ !=  CompletionItemType else type
        self.start = start
        self.length = length
        self.selectionStart = selectionStart
        self.selectionLength = selectionLength
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'label': self.label,
        }
        if self.text is not None:
            dct['text'] = self.text
        if self.sortText is not None:
            dct['sortText'] = self.sortText
        if self.type is not None:
            dct['type'] = self.type.to_dict()
        if self.start is not None:
            dct['start'] = self.start
        if self.length is not None:
            dct['length'] = self.length
        if self.selectionStart is not None:
            dct['selectionStart'] = self.selectionStart
        if self.selectionLength is not None:
            dct['selectionLength'] = self.selectionLength
        dct.update(self.kwargs)
        return dct


@register
class CompletionItemType(BaseSchema):
    """
    Some predefined types for the CompletionItem. Please note that not all clients have specific icons
    for all of them.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class ChecksumAlgorithm(BaseSchema):
    """
    Names of checksum algorithms that may be supported by a debug adapter.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class Checksum(BaseSchema):
    """
    The checksum of an item calculated by the specified algorithm.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "algorithm": {
            "description": "The algorithm used to calculate this checksum.",
            "type": "ChecksumAlgorithm"
        },
        "checksum": {
            "type": "string",
            "description": "Value of the checksum."
        }
    }
    __refs__ = {'algorithm'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, algorithm, checksum, **kwargs):
        """
        :param ChecksumAlgorithm algorithm: The algorithm used to calculate this checksum.
        :param string checksum: Value of the checksum.
        """
        if algorithm is None:
            self.algorithm = ChecksumAlgorithm()
        else:
            self.algorithm = ChecksumAlgorithm(**algorithm) if algorithm.__class__ !=  ChecksumAlgorithm else algorithm
        self.checksum = checksum
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'algorithm': self.algorithm.to_dict(),
             'checksum': self.checksum,
        }
        dct.update(self.kwargs)
        return dct


@register
class ValueFormat(BaseSchema):
    """
    Provides formatting information for a value.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "hex": {
            "type": "boolean",
            "description": "Display the value in hex."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, hex=None, **kwargs):
        """
        :param boolean hex: Display the value in hex.
        """
        self.hex = hex
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.hex is not None:
            dct['hex'] = self.hex
        dct.update(self.kwargs)
        return dct


@register
class StackFrameFormat(BaseSchema):
    """
    Provides formatting information for a stack frame.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "hex": {
            "type": "boolean",
            "description": "Display the value in hex."
        },
        "parameters": {
            "type": "boolean",
            "description": "Displays parameters for the stack frame."
        },
        "parameterTypes": {
            "type": "boolean",
            "description": "Displays the types of parameters for the stack frame."
        },
        "parameterNames": {
            "type": "boolean",
            "description": "Displays the names of parameters for the stack frame."
        },
        "parameterValues": {
            "type": "boolean",
            "description": "Displays the values of parameters for the stack frame."
        },
        "line": {
            "type": "boolean",
            "description": "Displays the line number of the stack frame."
        },
        "module": {
            "type": "boolean",
            "description": "Displays the module of the stack frame."
        },
        "includeAll": {
            "type": "boolean",
            "description": "Includes all stack frames, including those the debug adapter might otherwise hide."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, hex=None, parameters=None, parameterTypes=None, parameterNames=None, parameterValues=None, line=None, module=None, includeAll=None, **kwargs):
        """
        :param boolean hex: Display the value in hex.
        :param boolean parameters: Displays parameters for the stack frame.
        :param boolean parameterTypes: Displays the types of parameters for the stack frame.
        :param boolean parameterNames: Displays the names of parameters for the stack frame.
        :param boolean parameterValues: Displays the values of parameters for the stack frame.
        :param boolean line: Displays the line number of the stack frame.
        :param boolean module: Displays the module of the stack frame.
        :param boolean includeAll: Includes all stack frames, including those the debug adapter might otherwise hide.
        """
        self.hex = hex
        self.parameters = parameters
        self.parameterTypes = parameterTypes
        self.parameterNames = parameterNames
        self.parameterValues = parameterValues
        self.line = line
        self.module = module
        self.includeAll = includeAll
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.hex is not None:
            dct['hex'] = self.hex
        if self.parameters is not None:
            dct['parameters'] = self.parameters
        if self.parameterTypes is not None:
            dct['parameterTypes'] = self.parameterTypes
        if self.parameterNames is not None:
            dct['parameterNames'] = self.parameterNames
        if self.parameterValues is not None:
            dct['parameterValues'] = self.parameterValues
        if self.line is not None:
            dct['line'] = self.line
        if self.module is not None:
            dct['module'] = self.module
        if self.includeAll is not None:
            dct['includeAll'] = self.includeAll
        dct.update(self.kwargs)
        return dct


@register
class ExceptionOptions(BaseSchema):
    """
    An ExceptionOptions assigns configuration options to a set of exceptions.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "path": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ExceptionPathSegment"
            },
            "description": "A path that selects a single or multiple exceptions in a tree. If 'path' is missing, the whole tree is selected.\nBy convention the first segment of the path is a category that is used to group exceptions in the UI."
        },
        "breakMode": {
            "description": "Condition when a thrown exception should result in a break.",
            "type": "ExceptionBreakMode"
        }
    }
    __refs__ = {'breakMode'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakMode, path=None, **kwargs):
        """
        :param ExceptionBreakMode breakMode: Condition when a thrown exception should result in a break.
        :param array path: A path that selects a single or multiple exceptions in a tree. If 'path' is missing, the whole tree is selected.
        By convention the first segment of the path is a category that is used to group exceptions in the UI.
        """
        if breakMode is None:
            self.breakMode = ExceptionBreakMode()
        else:
            self.breakMode = ExceptionBreakMode(**breakMode) if breakMode.__class__ !=  ExceptionBreakMode else breakMode
        self.path = path
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakMode': self.breakMode.to_dict(),
        }
        if self.path is not None:
            dct['path'] = self.path
        dct.update(self.kwargs)
        return dct


@register
class ExceptionBreakMode(BaseSchema):
    """
    This enumeration defines all possible conditions when a thrown exception should result in a break.
    
    never: never breaks,
    
    always: always breaks,
    
    unhandled: breaks when exception unhandled,
    
    userUnhandled: breaks if the exception is not handled by user code.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class ExceptionPathSegment(BaseSchema):
    """
    An ExceptionPathSegment represents a segment in a path that is used to match leafs or nodes in a
    tree of exceptions.
    
    If a segment consists of more than one name, it matches the names provided if 'negate' is false or
    missing or
    
    it matches anything except the names provided if 'negate' is true.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "negate": {
            "type": "boolean",
            "description": "If false or missing this segment matches the names provided, otherwise it matches anything except the names provided."
        },
        "names": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Depending on the value of 'negate' the names that should match or not match."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, names, negate=None, **kwargs):
        """
        :param array names: Depending on the value of 'negate' the names that should match or not match.
        :param boolean negate: If false or missing this segment matches the names provided, otherwise it matches anything except the names provided.
        """
        self.names = names
        self.negate = negate
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'names': self.names,
        }
        if self.negate is not None:
            dct['negate'] = self.negate
        dct.update(self.kwargs)
        return dct


@register
class ExceptionDetails(BaseSchema):
    """
    Detailed information about an exception that has occurred.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "message": {
            "type": "string",
            "description": "Message contained in the exception."
        },
        "typeName": {
            "type": "string",
            "description": "Short type name of the exception object."
        },
        "fullTypeName": {
            "type": "string",
            "description": "Fully-qualified type name of the exception object."
        },
        "evaluateName": {
            "type": "string",
            "description": "Optional expression that can be evaluated in the current scope to obtain the exception object."
        },
        "stackTrace": {
            "type": "string",
            "description": "Stack trace at the time the exception was thrown."
        },
        "innerException": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/ExceptionDetails"
            },
            "description": "Details of the exception contained by this exception, if any."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, message=None, typeName=None, fullTypeName=None, evaluateName=None, stackTrace=None, innerException=None, **kwargs):
        """
        :param string message: Message contained in the exception.
        :param string typeName: Short type name of the exception object.
        :param string fullTypeName: Fully-qualified type name of the exception object.
        :param string evaluateName: Optional expression that can be evaluated in the current scope to obtain the exception object.
        :param string stackTrace: Stack trace at the time the exception was thrown.
        :param array innerException: Details of the exception contained by this exception, if any.
        """
        self.message = message
        self.typeName = typeName
        self.fullTypeName = fullTypeName
        self.evaluateName = evaluateName
        self.stackTrace = stackTrace
        self.innerException = innerException
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.typeName is not None:
            dct['typeName'] = self.typeName
        if self.fullTypeName is not None:
            dct['fullTypeName'] = self.fullTypeName
        if self.evaluateName is not None:
            dct['evaluateName'] = self.evaluateName
        if self.stackTrace is not None:
            dct['stackTrace'] = self.stackTrace
        if self.innerException is not None:
            dct['innerException'] = self.innerException
        dct.update(self.kwargs)
        return dct


@register
class DisassembledInstruction(BaseSchema):
    """
    Represents a single disassembled instruction.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "address": {
            "type": "string",
            "description": "The address of the instruction. Treated as a hex value if prefixed with '0x', or as a decimal value otherwise."
        },
        "instructionBytes": {
            "type": "string",
            "description": "Optional raw bytes representing the instruction and its operands, in an implementation-defined format."
        },
        "instruction": {
            "type": "string",
            "description": "Text representing the instruction and its operands, in an implementation-defined format."
        },
        "symbol": {
            "type": "string",
            "description": "Name of the symbol that corresponds with the location of this instruction, if any."
        },
        "location": {
            "description": "Source location that corresponds to this instruction, if any.\nShould always be set (if available) on the first instruction returned,\nbut can be omitted afterwards if this instruction maps to the same source file as the previous instruction.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "The line within the source location that corresponds to this instruction, if any."
        },
        "column": {
            "type": "integer",
            "description": "The column within the line that corresponds to this instruction, if any."
        },
        "endLine": {
            "type": "integer",
            "description": "The end line of the range that corresponds to this instruction, if any."
        },
        "endColumn": {
            "type": "integer",
            "description": "The end column of the range that corresponds to this instruction, if any."
        }
    }
    __refs__ = {'location'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, address, instruction, instructionBytes=None, symbol=None, location=None, line=None, column=None, endLine=None, endColumn=None, **kwargs):
        """
        :param string address: The address of the instruction. Treated as a hex value if prefixed with '0x', or as a decimal value otherwise.
        :param string instruction: Text representing the instruction and its operands, in an implementation-defined format.
        :param string instructionBytes: Optional raw bytes representing the instruction and its operands, in an implementation-defined format.
        :param string symbol: Name of the symbol that corresponds with the location of this instruction, if any.
        :param Source location: Source location that corresponds to this instruction, if any.
        Should always be set (if available) on the first instruction returned,
        but can be omitted afterwards if this instruction maps to the same source file as the previous instruction.
        :param integer line: The line within the source location that corresponds to this instruction, if any.
        :param integer column: The column within the line that corresponds to this instruction, if any.
        :param integer endLine: The end line of the range that corresponds to this instruction, if any.
        :param integer endColumn: The end column of the range that corresponds to this instruction, if any.
        """
        self.address = address
        self.instruction = instruction
        self.instructionBytes = instructionBytes
        self.symbol = symbol
        if location is None:
            self.location = Source()
        else:
            self.location = Source(**location) if location.__class__ !=  Source else location
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'address': self.address,
             'instruction': self.instruction,
        }
        if self.instructionBytes is not None:
            dct['instructionBytes'] = self.instructionBytes
        if self.symbol is not None:
            dct['symbol'] = self.symbol
        if self.location is not None:
            dct['location'] = self.location.to_dict()
        if self.line is not None:
            dct['line'] = self.line
        if self.column is not None:
            dct['column'] = self.column
        if self.endLine is not None:
            dct['endLine'] = self.endLine
        if self.endColumn is not None:
            dct['endColumn'] = self.endColumn
        dct.update(self.kwargs)
        return dct


@register
class InvalidatedAreas(BaseSchema):
    """
    Logical areas that can be invalidated by the 'invalidated' event.

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class ErrorResponseBody(BaseSchema):
    """
    "body" of ErrorResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "error": {
            "description": "An optional, structured error message.",
            "type": "Message"
        }
    }
    __refs__ = {'error'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, error=None, **kwargs):
        """
        :param Message error: An optional, structured error message.
        """
        if error is None:
            self.error = Message()
        else:
            self.error = Message(**error) if error.__class__ !=  Message else error
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.error is not None:
            dct['error'] = self.error.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class StoppedEventBody(BaseSchema):
    """
    "body" of StoppedEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "reason": {
            "type": "string",
            "description": "The reason for the event.\nFor backward compatibility this string is shown in the UI if the 'description' attribute is missing (but it must not be translated).",
            "_enum": [
                "step",
                "breakpoint",
                "exception",
                "pause",
                "entry",
                "goto",
                "function breakpoint",
                "data breakpoint",
                "instruction breakpoint"
            ]
        },
        "description": {
            "type": "string",
            "description": "The full reason for the event, e.g. 'Paused on exception'. This string is shown in the UI as is and must be translated."
        },
        "threadId": {
            "type": "integer",
            "description": "The thread which was stopped."
        },
        "preserveFocusHint": {
            "type": "boolean",
            "description": "A value of true hints to the frontend that this event should not change the focus."
        },
        "text": {
            "type": "string",
            "description": "Additional information. E.g. if reason is 'exception', text contains the exception name. This string is shown in the UI."
        },
        "allThreadsStopped": {
            "type": "boolean",
            "description": "If 'allThreadsStopped' is true, a debug adapter can announce that all threads have stopped.\n- The client should use this information to enable that all threads can be expanded to access their stacktraces.\n- If the attribute is missing or false, only the thread with the given threadId can be expanded."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, reason, description=None, threadId=None, preserveFocusHint=None, text=None, allThreadsStopped=None, **kwargs):
        """
        :param string reason: The reason for the event.
        For backward compatibility this string is shown in the UI if the 'description' attribute is missing (but it must not be translated).
        :param string description: The full reason for the event, e.g. 'Paused on exception'. This string is shown in the UI as is and must be translated.
        :param integer threadId: The thread which was stopped.
        :param boolean preserveFocusHint: A value of true hints to the frontend that this event should not change the focus.
        :param string text: Additional information. E.g. if reason is 'exception', text contains the exception name. This string is shown in the UI.
        :param boolean allThreadsStopped: If 'allThreadsStopped' is true, a debug adapter can announce that all threads have stopped.
        - The client should use this information to enable that all threads can be expanded to access their stacktraces.
        - If the attribute is missing or false, only the thread with the given threadId can be expanded.
        """
        self.reason = reason
        self.description = description
        self.threadId = threadId
        self.preserveFocusHint = preserveFocusHint
        self.text = text
        self.allThreadsStopped = allThreadsStopped
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'reason': self.reason,
        }
        if self.description is not None:
            dct['description'] = self.description
        if self.threadId is not None:
            dct['threadId'] = self.threadId
        if self.preserveFocusHint is not None:
            dct['preserveFocusHint'] = self.preserveFocusHint
        if self.text is not None:
            dct['text'] = self.text
        if self.allThreadsStopped is not None:
            dct['allThreadsStopped'] = self.allThreadsStopped
        dct.update(self.kwargs)
        return dct


@register
class ContinuedEventBody(BaseSchema):
    """
    "body" of ContinuedEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threadId": {
            "type": "integer",
            "description": "The thread which was continued."
        },
        "allThreadsContinued": {
            "type": "boolean",
            "description": "If 'allThreadsContinued' is true, a debug adapter can announce that all threads have continued."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threadId, allThreadsContinued=None, **kwargs):
        """
        :param integer threadId: The thread which was continued.
        :param boolean allThreadsContinued: If 'allThreadsContinued' is true, a debug adapter can announce that all threads have continued.
        """
        self.threadId = threadId
        self.allThreadsContinued = allThreadsContinued
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threadId': self.threadId,
        }
        if self.allThreadsContinued is not None:
            dct['allThreadsContinued'] = self.allThreadsContinued
        dct.update(self.kwargs)
        return dct


@register
class ExitedEventBody(BaseSchema):
    """
    "body" of ExitedEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "exitCode": {
            "type": "integer",
            "description": "The exit code returned from the debuggee."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, exitCode, **kwargs):
        """
        :param integer exitCode: The exit code returned from the debuggee.
        """
        self.exitCode = exitCode
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'exitCode': self.exitCode,
        }
        dct.update(self.kwargs)
        return dct


@register
class TerminatedEventBody(BaseSchema):
    """
    "body" of TerminatedEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "restart": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "A debug adapter may set 'restart' to true (or to an arbitrary object) to request that the front end restarts the session.\nThe value is not interpreted by the client and passed unmodified as an attribute '__restart' to the 'launch' and 'attach' requests."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, restart=None, **kwargs):
        """
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] restart: A debug adapter may set 'restart' to true (or to an arbitrary object) to request that the front end restarts the session.
        The value is not interpreted by the client and passed unmodified as an attribute '__restart' to the 'launch' and 'attach' requests.
        """
        self.restart = restart
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.restart is not None:
            dct['restart'] = self.restart
        dct.update(self.kwargs)
        return dct


@register
class ThreadEventBody(BaseSchema):
    """
    "body" of ThreadEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "reason": {
            "type": "string",
            "description": "The reason for the event.",
            "_enum": [
                "started",
                "exited"
            ]
        },
        "threadId": {
            "type": "integer",
            "description": "The identifier of the thread."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, reason, threadId, **kwargs):
        """
        :param string reason: The reason for the event.
        :param integer threadId: The identifier of the thread.
        """
        self.reason = reason
        self.threadId = threadId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'reason': self.reason,
             'threadId': self.threadId,
        }
        dct.update(self.kwargs)
        return dct


@register
class OutputEventBody(BaseSchema):
    """
    "body" of OutputEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "category": {
            "type": "string",
            "description": "The output category. If not specified, 'console' is assumed.",
            "_enum": [
                "console",
                "stdout",
                "stderr",
                "telemetry"
            ]
        },
        "output": {
            "type": "string",
            "description": "The output to report."
        },
        "group": {
            "type": "string",
            "description": "Support for keeping an output log organized by grouping related messages.",
            "enum": [
                "start",
                "startCollapsed",
                "end"
            ],
            "enumDescriptions": [
                "Start a new group in expanded mode. Subsequent output events are members of the group and should be shown indented.\nThe 'output' attribute becomes the name of the group and is not indented.",
                "Start a new group in collapsed mode. Subsequent output events are members of the group and should be shown indented (as soon as the group is expanded).\nThe 'output' attribute becomes the name of the group and is not indented.",
                "End the current group and decreases the indentation of subsequent output events.\nA non empty 'output' attribute is shown as the unindented end of the group."
            ]
        },
        "variablesReference": {
            "type": "integer",
            "description": "If an attribute 'variablesReference' exists and its value is > 0, the output contains objects which can be retrieved by passing 'variablesReference' to the 'variables' request. The value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "source": {
            "description": "An optional source location where the output was produced.",
            "type": "Source"
        },
        "line": {
            "type": "integer",
            "description": "An optional source location line where the output was produced."
        },
        "column": {
            "type": "integer",
            "description": "An optional source location column where the output was produced."
        },
        "data": {
            "type": [
                "array",
                "boolean",
                "integer",
                "null",
                "number",
                "object",
                "string"
            ],
            "description": "Optional data to report. For the 'telemetry' category the data will be sent to telemetry, for the other categories the data is shown in JSON format."
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, output, category=None, group=None, variablesReference=None, source=None, line=None, column=None, data=None, **kwargs):
        """
        :param string output: The output to report.
        :param string category: The output category. If not specified, 'console' is assumed.
        :param string group: Support for keeping an output log organized by grouping related messages.
        :param integer variablesReference: If an attribute 'variablesReference' exists and its value is > 0, the output contains objects which can be retrieved by passing 'variablesReference' to the 'variables' request. The value should be less than or equal to 2147483647 (2^31 - 1).
        :param Source source: An optional source location where the output was produced.
        :param integer line: An optional source location line where the output was produced.
        :param integer column: An optional source location column where the output was produced.
        :param ['array', 'boolean', 'integer', 'null', 'number', 'object', 'string'] data: Optional data to report. For the 'telemetry' category the data will be sent to telemetry, for the other categories the data is shown in JSON format.
        """
        self.output = output
        self.category = category
        self.group = group
        self.variablesReference = variablesReference
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.line = line
        self.column = column
        self.data = data
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'output': self.output,
        }
        if self.category is not None:
            dct['category'] = self.category
        if self.group is not None:
            dct['group'] = self.group
        if self.variablesReference is not None:
            dct['variablesReference'] = self.variablesReference
        if self.source is not None:
            dct['source'] = self.source.to_dict()
        if self.line is not None:
            dct['line'] = self.line
        if self.column is not None:
            dct['column'] = self.column
        if self.data is not None:
            dct['data'] = self.data
        dct.update(self.kwargs)
        return dct


@register
class BreakpointEventBody(BaseSchema):
    """
    "body" of BreakpointEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "reason": {
            "type": "string",
            "description": "The reason for the event.",
            "_enum": [
                "changed",
                "new",
                "removed"
            ]
        },
        "breakpoint": {
            "description": "The 'id' attribute is used to find the target breakpoint and the other attributes are used as the new values.",
            "type": "Breakpoint"
        }
    }
    __refs__ = {'breakpoint'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, reason, breakpoint, **kwargs):
        """
        :param string reason: The reason for the event.
        :param Breakpoint breakpoint: The 'id' attribute is used to find the target breakpoint and the other attributes are used as the new values.
        """
        self.reason = reason
        if breakpoint is None:
            self.breakpoint = Breakpoint()
        else:
            self.breakpoint = Breakpoint(**breakpoint) if breakpoint.__class__ !=  Breakpoint else breakpoint
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'reason': self.reason,
             'breakpoint': self.breakpoint.to_dict(),
        }
        dct.update(self.kwargs)
        return dct


@register
class ModuleEventBody(BaseSchema):
    """
    "body" of ModuleEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "reason": {
            "type": "string",
            "description": "The reason for the event.",
            "enum": [
                "new",
                "changed",
                "removed"
            ]
        },
        "module": {
            "description": "The new, changed, or removed module. In case of 'removed' only the module id is used.",
            "type": "Module"
        }
    }
    __refs__ = {'module'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, reason, module, **kwargs):
        """
        :param string reason: The reason for the event.
        :param Module module: The new, changed, or removed module. In case of 'removed' only the module id is used.
        """
        self.reason = reason
        if module is None:
            self.module = Module()
        else:
            self.module = Module(**module) if module.__class__ !=  Module else module
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'reason': self.reason,
             'module': self.module.to_dict(),
        }
        dct.update(self.kwargs)
        return dct


@register
class LoadedSourceEventBody(BaseSchema):
    """
    "body" of LoadedSourceEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "reason": {
            "type": "string",
            "description": "The reason for the event.",
            "enum": [
                "new",
                "changed",
                "removed"
            ]
        },
        "source": {
            "description": "The new, changed, or removed source.",
            "type": "Source"
        }
    }
    __refs__ = {'source'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, reason, source, **kwargs):
        """
        :param string reason: The reason for the event.
        :param Source source: The new, changed, or removed source.
        """
        self.reason = reason
        if source is None:
            self.source = Source()
        else:
            self.source = Source(**source) if source.__class__ !=  Source else source
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'reason': self.reason,
             'source': self.source.to_dict(),
        }
        dct.update(self.kwargs)
        return dct


@register
class ProcessEventBody(BaseSchema):
    """
    "body" of ProcessEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "name": {
            "type": "string",
            "description": "The logical name of the process. This is usually the full path to process's executable file. Example: /home/example/myproj/program.js."
        },
        "systemProcessId": {
            "type": "integer",
            "description": "The system process id of the debugged process. This property will be missing for non-system processes."
        },
        "isLocalProcess": {
            "type": "boolean",
            "description": "If true, the process is running on the same computer as the debug adapter."
        },
        "startMethod": {
            "type": "string",
            "enum": [
                "launch",
                "attach",
                "attachForSuspendedLaunch"
            ],
            "description": "Describes how the debug engine started debugging this process.",
            "enumDescriptions": [
                "Process was launched under the debugger.",
                "Debugger attached to an existing process.",
                "A project launcher component has launched a new process in a suspended state and then asked the debugger to attach."
            ]
        },
        "pointerSize": {
            "type": "integer",
            "description": "The size of a pointer or address for this process, in bits. This value may be used by clients when formatting addresses for display."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, name, systemProcessId=None, isLocalProcess=None, startMethod=None, pointerSize=None, **kwargs):
        """
        :param string name: The logical name of the process. This is usually the full path to process's executable file. Example: /home/example/myproj/program.js.
        :param integer systemProcessId: The system process id of the debugged process. This property will be missing for non-system processes.
        :param boolean isLocalProcess: If true, the process is running on the same computer as the debug adapter.
        :param string startMethod: Describes how the debug engine started debugging this process.
        :param integer pointerSize: The size of a pointer or address for this process, in bits. This value may be used by clients when formatting addresses for display.
        """
        self.name = name
        self.systemProcessId = systemProcessId
        self.isLocalProcess = isLocalProcess
        self.startMethod = startMethod
        self.pointerSize = pointerSize
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'name': self.name,
        }
        if self.systemProcessId is not None:
            dct['systemProcessId'] = self.systemProcessId
        if self.isLocalProcess is not None:
            dct['isLocalProcess'] = self.isLocalProcess
        if self.startMethod is not None:
            dct['startMethod'] = self.startMethod
        if self.pointerSize is not None:
            dct['pointerSize'] = self.pointerSize
        dct.update(self.kwargs)
        return dct


@register
class CapabilitiesEventBody(BaseSchema):
    """
    "body" of CapabilitiesEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "capabilities": {
            "description": "The set of updated capabilities.",
            "type": "Capabilities"
        }
    }
    __refs__ = {'capabilities'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, capabilities, **kwargs):
        """
        :param Capabilities capabilities: The set of updated capabilities.
        """
        if capabilities is None:
            self.capabilities = Capabilities()
        else:
            self.capabilities = Capabilities(**capabilities) if capabilities.__class__ !=  Capabilities else capabilities
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'capabilities': self.capabilities.to_dict(),
        }
        dct.update(self.kwargs)
        return dct


@register
class ProgressStartEventBody(BaseSchema):
    """
    "body" of ProgressStartEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "progressId": {
            "type": "string",
            "description": "An ID that must be used in subsequent 'progressUpdate' and 'progressEnd' events to make them refer to the same progress reporting.\nIDs must be unique within a debug session."
        },
        "title": {
            "type": "string",
            "description": "Mandatory (short) title of the progress reporting. Shown in the UI to describe the long running operation."
        },
        "requestId": {
            "type": "number",
            "description": "The request ID that this progress report is related to. If specified a debug adapter is expected to emit\nprogress events for the long running request until the request has been either completed or cancelled.\nIf the request ID is omitted, the progress report is assumed to be related to some general activity of the debug adapter."
        },
        "cancellable": {
            "type": "boolean",
            "description": "If true, the request that reports progress may be canceled with a 'cancel' request.\nSo this property basically controls whether the client should use UX that supports cancellation.\nClients that don't support cancellation are allowed to ignore the setting."
        },
        "message": {
            "type": "string",
            "description": "Optional, more detailed progress message."
        },
        "percentage": {
            "type": "number",
            "description": "Optional progress percentage to display (value range: 0 to 100). If omitted no percentage will be shown."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, progressId, title, requestId=None, cancellable=None, message=None, percentage=None, **kwargs):
        """
        :param string progressId: An ID that must be used in subsequent 'progressUpdate' and 'progressEnd' events to make them refer to the same progress reporting.
        IDs must be unique within a debug session.
        :param string title: Mandatory (short) title of the progress reporting. Shown in the UI to describe the long running operation.
        :param number requestId: The request ID that this progress report is related to. If specified a debug adapter is expected to emit
        progress events for the long running request until the request has been either completed or cancelled.
        If the request ID is omitted, the progress report is assumed to be related to some general activity of the debug adapter.
        :param boolean cancellable: If true, the request that reports progress may be canceled with a 'cancel' request.
        So this property basically controls whether the client should use UX that supports cancellation.
        Clients that don't support cancellation are allowed to ignore the setting.
        :param string message: Optional, more detailed progress message.
        :param number percentage: Optional progress percentage to display (value range: 0 to 100). If omitted no percentage will be shown.
        """
        self.progressId = progressId
        self.title = title
        self.requestId = requestId
        self.cancellable = cancellable
        self.message = message
        self.percentage = percentage
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'progressId': self.progressId,
             'title': self.title,
        }
        if self.requestId is not None:
            dct['requestId'] = self.requestId
        if self.cancellable is not None:
            dct['cancellable'] = self.cancellable
        if self.message is not None:
            dct['message'] = self.message
        if self.percentage is not None:
            dct['percentage'] = self.percentage
        dct.update(self.kwargs)
        return dct


@register
class ProgressUpdateEventBody(BaseSchema):
    """
    "body" of ProgressUpdateEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "progressId": {
            "type": "string",
            "description": "The ID that was introduced in the initial 'progressStart' event."
        },
        "message": {
            "type": "string",
            "description": "Optional, more detailed progress message. If omitted, the previous message (if any) is used."
        },
        "percentage": {
            "type": "number",
            "description": "Optional progress percentage to display (value range: 0 to 100). If omitted no percentage will be shown."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, progressId, message=None, percentage=None, **kwargs):
        """
        :param string progressId: The ID that was introduced in the initial 'progressStart' event.
        :param string message: Optional, more detailed progress message. If omitted, the previous message (if any) is used.
        :param number percentage: Optional progress percentage to display (value range: 0 to 100). If omitted no percentage will be shown.
        """
        self.progressId = progressId
        self.message = message
        self.percentage = percentage
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'progressId': self.progressId,
        }
        if self.message is not None:
            dct['message'] = self.message
        if self.percentage is not None:
            dct['percentage'] = self.percentage
        dct.update(self.kwargs)
        return dct


@register
class ProgressEndEventBody(BaseSchema):
    """
    "body" of ProgressEndEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "progressId": {
            "type": "string",
            "description": "The ID that was introduced in the initial 'ProgressStartEvent'."
        },
        "message": {
            "type": "string",
            "description": "Optional, more detailed progress message. If omitted, the previous message (if any) is used."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, progressId, message=None, **kwargs):
        """
        :param string progressId: The ID that was introduced in the initial 'ProgressStartEvent'.
        :param string message: Optional, more detailed progress message. If omitted, the previous message (if any) is used.
        """
        self.progressId = progressId
        self.message = message
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'progressId': self.progressId,
        }
        if self.message is not None:
            dct['message'] = self.message
        dct.update(self.kwargs)
        return dct


@register
class InvalidatedEventBody(BaseSchema):
    """
    "body" of InvalidatedEvent

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "areas": {
            "type": "array",
            "description": "Optional set of logical areas that got invalidated. This property has a hint characteristic: a client can only be expected to make a 'best effort' in honouring the areas but there are no guarantees. If this property is missing, empty, or if values are not understand the client should assume a single value 'all'.",
            "items": {
                "$ref": "#/definitions/InvalidatedAreas"
            }
        },
        "threadId": {
            "type": "number",
            "description": "If specified, the client only needs to refetch data related to this thread."
        },
        "stackFrameId": {
            "type": "number",
            "description": "If specified, the client only needs to refetch data related to this stack frame (and the 'threadId' is ignored)."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, areas=None, threadId=None, stackFrameId=None, **kwargs):
        """
        :param array areas: Optional set of logical areas that got invalidated. This property has a hint characteristic: a client can only be expected to make a 'best effort' in honouring the areas but there are no guarantees. If this property is missing, empty, or if values are not understand the client should assume a single value 'all'.
        :param number threadId: If specified, the client only needs to refetch data related to this thread.
        :param number stackFrameId: If specified, the client only needs to refetch data related to this stack frame (and the 'threadId' is ignored).
        """
        self.areas = areas
        self.threadId = threadId
        self.stackFrameId = stackFrameId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.areas is not None:
            dct['areas'] = self.areas
        if self.threadId is not None:
            dct['threadId'] = self.threadId
        if self.stackFrameId is not None:
            dct['stackFrameId'] = self.stackFrameId
        dct.update(self.kwargs)
        return dct


@register
class RunInTerminalRequestArgumentsEnv(BaseSchema):
    """
    "env" of RunInTerminalRequestArguments

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct


@register
class RunInTerminalResponseBody(BaseSchema):
    """
    "body" of RunInTerminalResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "processId": {
            "type": "integer",
            "description": "The process ID. The value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "shellProcessId": {
            "type": "integer",
            "description": "The process ID of the terminal shell. The value should be less than or equal to 2147483647 (2^31 - 1)."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, processId=None, shellProcessId=None, **kwargs):
        """
        :param integer processId: The process ID. The value should be less than or equal to 2147483647 (2^31 - 1).
        :param integer shellProcessId: The process ID of the terminal shell. The value should be less than or equal to 2147483647 (2^31 - 1).
        """
        self.processId = processId
        self.shellProcessId = shellProcessId
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.processId is not None:
            dct['processId'] = self.processId
        if self.shellProcessId is not None:
            dct['shellProcessId'] = self.shellProcessId
        dct.update(self.kwargs)
        return dct


@register
class BreakpointLocationsResponseBody(BaseSchema):
    """
    "body" of BreakpointLocationsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/BreakpointLocation"
            },
            "description": "Sorted set of possible breakpoint locations."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: Sorted set of possible breakpoint locations.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetBreakpointsResponseBody(BaseSchema):
    """
    "body" of SetBreakpointsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Breakpoint"
            },
            "description": "Information about the breakpoints.\nThe array elements are in the same order as the elements of the 'breakpoints' (or the deprecated 'lines') array in the arguments."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: Information about the breakpoints.
        The array elements are in the same order as the elements of the 'breakpoints' (or the deprecated 'lines') array in the arguments.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetFunctionBreakpointsResponseBody(BaseSchema):
    """
    "body" of SetFunctionBreakpointsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Breakpoint"
            },
            "description": "Information about the breakpoints. The array elements correspond to the elements of the 'breakpoints' array."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: Information about the breakpoints. The array elements correspond to the elements of the 'breakpoints' array.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register
class DataBreakpointInfoResponseBody(BaseSchema):
    """
    "body" of DataBreakpointInfoResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "dataId": {
            "type": [
                "string",
                "null"
            ],
            "description": "An identifier for the data on which a data breakpoint can be registered with the setDataBreakpoints request or null if no data breakpoint is available."
        },
        "description": {
            "type": "string",
            "description": "UI string that describes on what data the breakpoint is set on or why a data breakpoint is not available."
        },
        "accessTypes": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/DataBreakpointAccessType"
            },
            "description": "Optional attribute listing the available access types for a potential data breakpoint. A UI frontend could surface this information."
        },
        "canPersist": {
            "type": "boolean",
            "description": "Optional attribute indicating that a potential data breakpoint could be persisted across sessions."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, dataId, description, accessTypes=None, canPersist=None, **kwargs):
        """
        :param ['string', 'null'] dataId: An identifier for the data on which a data breakpoint can be registered with the setDataBreakpoints request or null if no data breakpoint is available.
        :param string description: UI string that describes on what data the breakpoint is set on or why a data breakpoint is not available.
        :param array accessTypes: Optional attribute listing the available access types for a potential data breakpoint. A UI frontend could surface this information.
        :param boolean canPersist: Optional attribute indicating that a potential data breakpoint could be persisted across sessions.
        """
        self.dataId = dataId
        self.description = description
        self.accessTypes = accessTypes
        self.canPersist = canPersist
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'dataId': self.dataId,
             'description': self.description,
        }
        if self.accessTypes is not None:
            dct['accessTypes'] = self.accessTypes
        if self.canPersist is not None:
            dct['canPersist'] = self.canPersist
        dct.update(self.kwargs)
        return dct


@register
class SetDataBreakpointsResponseBody(BaseSchema):
    """
    "body" of SetDataBreakpointsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Breakpoint"
            },
            "description": "Information about the data breakpoints. The array elements correspond to the elements of the input argument 'breakpoints' array."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: Information about the data breakpoints. The array elements correspond to the elements of the input argument 'breakpoints' array.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetInstructionBreakpointsResponseBody(BaseSchema):
    """
    "body" of SetInstructionBreakpointsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "breakpoints": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Breakpoint"
            },
            "description": "Information about the breakpoints. The array elements correspond to the elements of the 'breakpoints' array."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, breakpoints, **kwargs):
        """
        :param array breakpoints: Information about the breakpoints. The array elements correspond to the elements of the 'breakpoints' array.
        """
        self.breakpoints = breakpoints
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'breakpoints': self.breakpoints,
        }
        dct.update(self.kwargs)
        return dct


@register
class ContinueResponseBody(BaseSchema):
    """
    "body" of ContinueResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "allThreadsContinued": {
            "type": "boolean",
            "description": "If true, the 'continue' request has ignored the specified thread and continued all threads instead.\nIf this attribute is missing a value of 'true' is assumed for backward compatibility."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, allThreadsContinued=None, **kwargs):
        """
        :param boolean allThreadsContinued: If true, the 'continue' request has ignored the specified thread and continued all threads instead.
        If this attribute is missing a value of 'true' is assumed for backward compatibility.
        """
        self.allThreadsContinued = allThreadsContinued
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        if self.allThreadsContinued is not None:
            dct['allThreadsContinued'] = self.allThreadsContinued
        dct.update(self.kwargs)
        return dct


@register
class StackTraceResponseBody(BaseSchema):
    """
    "body" of StackTraceResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "stackFrames": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/StackFrame"
            },
            "description": "The frames of the stackframe. If the array has length zero, there are no stackframes available.\nThis means that there is no location information available."
        },
        "totalFrames": {
            "type": "integer",
            "description": "The total number of frames available."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, stackFrames, totalFrames=None, **kwargs):
        """
        :param array stackFrames: The frames of the stackframe. If the array has length zero, there are no stackframes available.
        This means that there is no location information available.
        :param integer totalFrames: The total number of frames available.
        """
        self.stackFrames = stackFrames
        self.totalFrames = totalFrames
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'stackFrames': self.stackFrames,
        }
        if self.totalFrames is not None:
            dct['totalFrames'] = self.totalFrames
        dct.update(self.kwargs)
        return dct


@register
class ScopesResponseBody(BaseSchema):
    """
    "body" of ScopesResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "scopes": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Scope"
            },
            "description": "The scopes of the stackframe. If the array has length zero, there are no scopes available."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, scopes, **kwargs):
        """
        :param array scopes: The scopes of the stackframe. If the array has length zero, there are no scopes available.
        """
        self.scopes = scopes
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'scopes': self.scopes,
        }
        dct.update(self.kwargs)
        return dct


@register
class VariablesResponseBody(BaseSchema):
    """
    "body" of VariablesResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "variables": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Variable"
            },
            "description": "All (or a range) of variables for the given variable reference."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, variables, **kwargs):
        """
        :param array variables: All (or a range) of variables for the given variable reference.
        """
        self.variables = variables
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'variables': self.variables,
        }
        dct.update(self.kwargs)
        return dct


@register
class SetVariableResponseBody(BaseSchema):
    """
    "body" of SetVariableResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "value": {
            "type": "string",
            "description": "The new value of the variable."
        },
        "type": {
            "type": "string",
            "description": "The type of the new value. Typically shown in the UI when hovering over the value."
        },
        "variablesReference": {
            "type": "integer",
            "description": "If variablesReference is > 0, the new value is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "namedVariables": {
            "type": "integer",
            "description": "The number of named child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "indexedVariables": {
            "type": "integer",
            "description": "The number of indexed child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, value, type=None, variablesReference=None, namedVariables=None, indexedVariables=None, **kwargs):
        """
        :param string value: The new value of the variable.
        :param string type: The type of the new value. Typically shown in the UI when hovering over the value.
        :param integer variablesReference: If variablesReference is > 0, the new value is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param integer namedVariables: The number of named child variables.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param integer indexedVariables: The number of indexed child variables.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        """
        self.value = value
        self.type = type
        self.variablesReference = variablesReference
        self.namedVariables = namedVariables
        self.indexedVariables = indexedVariables
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'value': self.value,
        }
        if self.type is not None:
            dct['type'] = self.type
        if self.variablesReference is not None:
            dct['variablesReference'] = self.variablesReference
        if self.namedVariables is not None:
            dct['namedVariables'] = self.namedVariables
        if self.indexedVariables is not None:
            dct['indexedVariables'] = self.indexedVariables
        dct.update(self.kwargs)
        return dct


@register
class SourceResponseBody(BaseSchema):
    """
    "body" of SourceResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "content": {
            "type": "string",
            "description": "Content of the source reference."
        },
        "mimeType": {
            "type": "string",
            "description": "Optional content type (mime type) of the source."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, content, mimeType=None, **kwargs):
        """
        :param string content: Content of the source reference.
        :param string mimeType: Optional content type (mime type) of the source.
        """
        self.content = content
        self.mimeType = mimeType
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'content': self.content,
        }
        if self.mimeType is not None:
            dct['mimeType'] = self.mimeType
        dct.update(self.kwargs)
        return dct


@register
class ThreadsResponseBody(BaseSchema):
    """
    "body" of ThreadsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "threads": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Thread"
            },
            "description": "All threads."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, threads, **kwargs):
        """
        :param array threads: All threads.
        """
        self.threads = threads
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'threads': self.threads,
        }
        dct.update(self.kwargs)
        return dct


@register
class ModulesResponseBody(BaseSchema):
    """
    "body" of ModulesResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "modules": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Module"
            },
            "description": "All modules or range of modules."
        },
        "totalModules": {
            "type": "integer",
            "description": "The total number of modules available."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, modules, totalModules=None, **kwargs):
        """
        :param array modules: All modules or range of modules.
        :param integer totalModules: The total number of modules available.
        """
        self.modules = modules
        self.totalModules = totalModules
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'modules': self.modules,
        }
        if self.totalModules is not None:
            dct['totalModules'] = self.totalModules
        dct.update(self.kwargs)
        return dct


@register
class LoadedSourcesResponseBody(BaseSchema):
    """
    "body" of LoadedSourcesResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "sources": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Source"
            },
            "description": "Set of loaded sources."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, sources, **kwargs):
        """
        :param array sources: Set of loaded sources.
        """
        self.sources = sources
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'sources': self.sources,
        }
        dct.update(self.kwargs)
        return dct


@register
class EvaluateResponseBody(BaseSchema):
    """
    "body" of EvaluateResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "result": {
            "type": "string",
            "description": "The result of the evaluate request."
        },
        "type": {
            "type": "string",
            "description": "The optional type of the evaluate result.\nThis attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request."
        },
        "presentationHint": {
            "description": "Properties of a evaluate result that can be used to determine how to render the result in the UI.",
            "type": "VariablePresentationHint"
        },
        "variablesReference": {
            "type": "integer",
            "description": "If variablesReference is > 0, the evaluate result is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "namedVariables": {
            "type": "integer",
            "description": "The number of named child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "indexedVariables": {
            "type": "integer",
            "description": "The number of indexed child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "memoryReference": {
            "type": "string",
            "description": "Optional memory reference to a location appropriate for this result.\nFor pointer type eval results, this is generally a reference to the memory address contained in the pointer.\nThis attribute should be returned by a debug adapter if the client has passed the value true for the 'supportsMemoryReferences' capability of the 'initialize' request."
        }
    }
    __refs__ = {'presentationHint'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, result, variablesReference, type=None, presentationHint=None, namedVariables=None, indexedVariables=None, memoryReference=None, **kwargs):
        """
        :param string result: The result of the evaluate request.
        :param integer variablesReference: If variablesReference is > 0, the evaluate result is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param string type: The optional type of the evaluate result.
        This attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request.
        :param VariablePresentationHint presentationHint: Properties of a evaluate result that can be used to determine how to render the result in the UI.
        :param integer namedVariables: The number of named child variables.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param integer indexedVariables: The number of indexed child variables.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param string memoryReference: Optional memory reference to a location appropriate for this result.
        For pointer type eval results, this is generally a reference to the memory address contained in the pointer.
        This attribute should be returned by a debug adapter if the client has passed the value true for the 'supportsMemoryReferences' capability of the 'initialize' request.
        """
        self.result = result
        self.variablesReference = variablesReference
        self.type = type
        if presentationHint is None:
            self.presentationHint = VariablePresentationHint()
        else:
            self.presentationHint = VariablePresentationHint(**presentationHint) if presentationHint.__class__ !=  VariablePresentationHint else presentationHint
        self.namedVariables = namedVariables
        self.indexedVariables = indexedVariables
        self.memoryReference = memoryReference
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'result': self.result,
             'variablesReference': self.variablesReference,
        }
        if self.type is not None:
            dct['type'] = self.type
        if self.presentationHint is not None:
            dct['presentationHint'] = self.presentationHint.to_dict()
        if self.namedVariables is not None:
            dct['namedVariables'] = self.namedVariables
        if self.indexedVariables is not None:
            dct['indexedVariables'] = self.indexedVariables
        if self.memoryReference is not None:
            dct['memoryReference'] = self.memoryReference
        dct.update(self.kwargs)
        return dct


@register
class SetExpressionResponseBody(BaseSchema):
    """
    "body" of SetExpressionResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "value": {
            "type": "string",
            "description": "The new value of the expression."
        },
        "type": {
            "type": "string",
            "description": "The optional type of the value.\nThis attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request."
        },
        "presentationHint": {
            "description": "Properties of a value that can be used to determine how to render the result in the UI.",
            "type": "VariablePresentationHint"
        },
        "variablesReference": {
            "type": "integer",
            "description": "If variablesReference is > 0, the value is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "namedVariables": {
            "type": "integer",
            "description": "The number of named child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        },
        "indexedVariables": {
            "type": "integer",
            "description": "The number of indexed child variables.\nThe client can use this optional information to present the variables in a paged UI and fetch them in chunks.\nThe value should be less than or equal to 2147483647 (2^31 - 1)."
        }
    }
    __refs__ = {'presentationHint'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, value, type=None, presentationHint=None, variablesReference=None, namedVariables=None, indexedVariables=None, **kwargs):
        """
        :param string value: The new value of the expression.
        :param string type: The optional type of the value.
        This attribute should only be returned by a debug adapter if the client has passed the value true for the 'supportsVariableType' capability of the 'initialize' request.
        :param VariablePresentationHint presentationHint: Properties of a value that can be used to determine how to render the result in the UI.
        :param integer variablesReference: If variablesReference is > 0, the value is structured and its children can be retrieved by passing variablesReference to the VariablesRequest.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param integer namedVariables: The number of named child variables.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        :param integer indexedVariables: The number of indexed child variables.
        The client can use this optional information to present the variables in a paged UI and fetch them in chunks.
        The value should be less than or equal to 2147483647 (2^31 - 1).
        """
        self.value = value
        self.type = type
        if presentationHint is None:
            self.presentationHint = VariablePresentationHint()
        else:
            self.presentationHint = VariablePresentationHint(**presentationHint) if presentationHint.__class__ !=  VariablePresentationHint else presentationHint
        self.variablesReference = variablesReference
        self.namedVariables = namedVariables
        self.indexedVariables = indexedVariables
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'value': self.value,
        }
        if self.type is not None:
            dct['type'] = self.type
        if self.presentationHint is not None:
            dct['presentationHint'] = self.presentationHint.to_dict()
        if self.variablesReference is not None:
            dct['variablesReference'] = self.variablesReference
        if self.namedVariables is not None:
            dct['namedVariables'] = self.namedVariables
        if self.indexedVariables is not None:
            dct['indexedVariables'] = self.indexedVariables
        dct.update(self.kwargs)
        return dct


@register
class StepInTargetsResponseBody(BaseSchema):
    """
    "body" of StepInTargetsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "targets": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/StepInTarget"
            },
            "description": "The possible stepIn targets of the specified source location."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, targets, **kwargs):
        """
        :param array targets: The possible stepIn targets of the specified source location.
        """
        self.targets = targets
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'targets': self.targets,
        }
        dct.update(self.kwargs)
        return dct


@register
class GotoTargetsResponseBody(BaseSchema):
    """
    "body" of GotoTargetsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "targets": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/GotoTarget"
            },
            "description": "The possible goto targets of the specified location."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, targets, **kwargs):
        """
        :param array targets: The possible goto targets of the specified location.
        """
        self.targets = targets
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'targets': self.targets,
        }
        dct.update(self.kwargs)
        return dct


@register
class CompletionsResponseBody(BaseSchema):
    """
    "body" of CompletionsResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "targets": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/CompletionItem"
            },
            "description": "The possible completions for ."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, targets, **kwargs):
        """
        :param array targets: The possible completions for .
        """
        self.targets = targets
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'targets': self.targets,
        }
        dct.update(self.kwargs)
        return dct


@register
class ExceptionInfoResponseBody(BaseSchema):
    """
    "body" of ExceptionInfoResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "exceptionId": {
            "type": "string",
            "description": "ID of the exception that was thrown."
        },
        "description": {
            "type": "string",
            "description": "Descriptive text for the exception provided by the debug adapter."
        },
        "breakMode": {
            "description": "Mode that caused the exception notification to be raised.",
            "type": "ExceptionBreakMode"
        },
        "details": {
            "description": "Detailed information about the exception.",
            "type": "ExceptionDetails"
        }
    }
    __refs__ = {'breakMode', 'details'}

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, exceptionId, breakMode, description=None, details=None, **kwargs):
        """
        :param string exceptionId: ID of the exception that was thrown.
        :param ExceptionBreakMode breakMode: Mode that caused the exception notification to be raised.
        :param string description: Descriptive text for the exception provided by the debug adapter.
        :param ExceptionDetails details: Detailed information about the exception.
        """
        self.exceptionId = exceptionId
        if breakMode is None:
            self.breakMode = ExceptionBreakMode()
        else:
            self.breakMode = ExceptionBreakMode(**breakMode) if breakMode.__class__ !=  ExceptionBreakMode else breakMode
        self.description = description
        if details is None:
            self.details = ExceptionDetails()
        else:
            self.details = ExceptionDetails(**details) if details.__class__ !=  ExceptionDetails else details
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'exceptionId': self.exceptionId,
             'breakMode': self.breakMode.to_dict(),
        }
        if self.description is not None:
            dct['description'] = self.description
        if self.details is not None:
            dct['details'] = self.details.to_dict()
        dct.update(self.kwargs)
        return dct


@register
class ReadMemoryResponseBody(BaseSchema):
    """
    "body" of ReadMemoryResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "address": {
            "type": "string",
            "description": "The address of the first byte of data returned.\nTreated as a hex value if prefixed with '0x', or as a decimal value otherwise."
        },
        "unreadableBytes": {
            "type": "integer",
            "description": "The number of unreadable bytes encountered after the last successfully read byte.\nThis can be used to determine the number of bytes that must be skipped before a subsequent 'readMemory' request will succeed."
        },
        "data": {
            "type": "string",
            "description": "The bytes read from memory, encoded using base64."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, address, unreadableBytes=None, data=None, **kwargs):
        """
        :param string address: The address of the first byte of data returned.
        Treated as a hex value if prefixed with '0x', or as a decimal value otherwise.
        :param integer unreadableBytes: The number of unreadable bytes encountered after the last successfully read byte.
        This can be used to determine the number of bytes that must be skipped before a subsequent 'readMemory' request will succeed.
        :param string data: The bytes read from memory, encoded using base64.
        """
        self.address = address
        self.unreadableBytes = unreadableBytes
        self.data = data
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'address': self.address,
        }
        if self.unreadableBytes is not None:
            dct['unreadableBytes'] = self.unreadableBytes
        if self.data is not None:
            dct['data'] = self.data
        dct.update(self.kwargs)
        return dct


@register
class DisassembleResponseBody(BaseSchema):
    """
    "body" of DisassembleResponse

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {
        "instructions": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/DisassembledInstruction"
            },
            "description": "The list of disassembled instructions."
        }
    }
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, instructions, **kwargs):
        """
        :param array instructions: The list of disassembled instructions.
        """
        self.instructions = instructions
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
             'instructions': self.instructions,
        }
        dct.update(self.kwargs)
        return dct


@register
class MessageVariables(BaseSchema):
    """
    "variables" of Message

    Note: automatically generated code. Do not edit manually.
    """

    __props__ = {}
    __refs__ = set()

    __slots__ = list(__props__.keys()) + ['kwargs']

    def __init__(self, **kwargs):
        """
    
        """
    
        self.kwargs = kwargs


    def to_dict(self):
        dct = {
        }
        dct.update(self.kwargs)
        return dct
