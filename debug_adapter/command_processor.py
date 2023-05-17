# Copyright (c) 2019 Fabio Zadrozny
# Additions Copyright (c) 2020, Espressif Systems (Shanghai) Co. Ltd.
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

import json
from queue import Queue
from . import schema, base_schema, log
from .tools import get_good_path, Measurement
from .internal_classes import DaDevModes, DaRunState


POST_MORTEM_MODE_NOTIFICATION = "---\n" \
                                "Post-mortem mode! GDB functions changes state of the target are disabled.\n" \
                                "If you want to send a GDB command type `-exec COMMAND` to the Debug Console\n" \
                                "---\n"


class CommandProcessor(object):
    """
    This is the class that actually processes commands.

    It's created in the main thread and then control is passed on to the reader thread so that whenever
    something is read the json is handled by this processor.

    The queue it receives in the constructor should be used to talk to the writer thread, where it's expected
    to post protocol messages (which will be converted with 'to_dict()' and will have the 'seq' updated as
    needed).
    """

    def __init__(self, dbg_adapter_inst, write_queue, args):
        self.da = dbg_adapter_inst
        self.write_queue = write_queue  # type: Queue
        self.args = args  # type: tuple
        self._logger = log.new_logger("Debug Adapter(Command Processor)")
        self.evaluated = False
        self.evaluation_cache_exp = ""
        self.evaluation_cache_value = ""

    def __call__(self, protocol_message):
        self._logger.debug('Got json: %s' % (json.dumps(protocol_message.to_dict(), indent=4, sort_keys=True), ))

        try:
            if protocol_message.type == 'request':
                method_name = 'on_%s_request' % (protocol_message.command, )
                on_request = getattr(self, method_name, None)  # check if we have a method  method_name
                if on_request is not None:
                    on_request(protocol_message)
                else:
                    self._logger.warning('Unhandled: %s not available in CommandProcessor.' % (method_name, ))
                self._logger.debug("Processed command: %s" % protocol_message.command)
        except Exception as e:
            log.debug_exception(e)

    def on_initialize_request(self, request):
        """

        Parameters
        ----------
        request : schema.InitializeRequest

        """
        m = Measurement()
        response = base_schema.build_response(request)  # type: schema.InitializeResponse
        try:
            self.da.adapter_init()
        except Exception as e:
            response.success = False
            response.message = "Failed to init Debug Adapter!"
            self.write_message(response)
            raise e
        # response
        if self.da.args.postmortem:
            response.body.supportsConfigurationDoneRequest = True
            response.body.supportsRestartRequest = True

        else:
            # Supported features
            response.body.supportsConfigurationDoneRequest = True
            response.body.supportsConditionalBreakpoints = True
            response.body.supportsDataBreakpoints = True
            response.body.supportsHitConditionalBreakpoints = True
            response.body.supportsLogPoints = True
            response.body.supportsSetVariable = True
            response.body.supportsRestartRequest = True
            response.body.supportTerminateDebuggee = True
            response.body.supportsStepInTargetsRequest = True
            response.body.supportsDisassembleRequest = True
            response.body.supportsInstructionBreakpoints = True
            response.body.supportsReadMemoryRequest = True
            response.body.supportsSteppingGranularity = True
            # Not supported features
            response.body.supportsFunctionBreakpoints = False
            response.body.supportsEvaluateForHovers = False
            response.body.exceptionBreakpointFilters = False
            response.body.supportsStepBack = False
            response.body.supportsRestartFrame = False
            response.body.supportsGotoTargetsRequest = False
            response.body.supportsCompletionsRequest = False
            response.body.completionTriggerCharacters = False
            response.body.supportsModulesRequest = False
            response.body.additionalModuleColumns = False
            response.body.supportedChecksumAlgorithms = False
            response.body.supportsExceptionOptions = False
            response.body.supportsValueFormattingOptions = False
            response.body.supportsExceptionInfoRequest = False
            response.body.supportsDelayedStackTraceLoading = False
            response.body.supportsLoadedSourcesRequest = False
            response.body.supportsTerminateThreadsRequest = False
            response.body.supportsSetExpression = False
            response.body.supportsTerminateRequest = False
            response.body.supportsCancelRequest = False
            response.body.supportsBreakpointLocationsRequest = False
            response.body.supportsClipboardContext = False
        self.write_message(response)
        # done event
        self.write_message(schema.InitializedEvent())
        self.generate_OutputEvent("Debug Adapter initialized\n")
        if self.da.args.postmortem:
            self.da._gdb._target_state = 1
            self.generate_StoppedEvent(reason="exception",
                                       preserve_focus_hint=True,
                                       all_threads_stopped=True,
                                       thread_id=1)
        if self.da.args.developer_mode == DaDevModes.CON_CHECK:
            self.generate_TerminatedEvent()
        m.stop_n_check(2)

    def on_launch_request(self, request):
        """
        Parameters
        ----------
        request:schema.LaunchRequest
        """
        if self.da.args.developer_mode == DaDevModes.CON_CHECK:
            return
        # r_args = request.arguments.to_dict()
        self.da.state.no_debug = False  # BUG: r_args.get('noDebug') is always True coming from the extension !!!
        try:
            self.da.run(start=(not self.da.state.no_debug))
            success = True
        except Exception as e:
            log.debug_exception(e)
            success = False
        launch_response = base_schema.build_response(request)
        launch_response.success = success
        self.write_message(launch_response)  # acknowledge it
        if success:
            self.generate_OutputEvent("Debug Adapter is running\n")
        else:
            self.generate_OutputEvent("Debug Adapter is not running\n")

    def on_configurationDone_request(self, request):
        """
        Parameters
        ----------
        request:schema.ConfigurationDoneRequest
        """
        self.da.state.run_state = DaRunState.CONFIGURED
        configuration_done_response = base_schema.build_response(request)
        self.write_message(configuration_done_response)  # acknowledge it
        if self.da.state.no_debug:
            self.da.adapter_stop()
            self.generate_TerminatedEvent(restart=False)

    def generate_TerminatedEvent(self, restart=False):
        """
        Parameters
        ----------
        restart : bool
            asks for restart
        """
        body = schema.TerminatedEventBody(restart=restart)
        event = schema.TerminatedEvent(body=body)
        self.write_message(event)

    def on_restart_request(self, request):
        """
        Parameters
        ----------
        request: schema.RestartRequest
        """
        response = base_schema.build_response(request)
        for th in self.da.get_thread_list():
            id = th.get('id')
            self.generate_ThreadEvent(thread_id=int(id), reason='exited')
        self.da.gdb_restart()
        self.da.start()
        self.write_message(response)

    def on_continue_request(self, request):
        """
        Parameters
        ----------
        request : schema.ContinueRequest
        """
        if self.da.args.postmortem:
            kwargs = {'body': schema.ContinueResponseBody()}
            response = base_schema.build_response(request, kwargs)
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            self.da.resume_exec()
            kwargs = {'body': schema.ContinueResponseBody(allThreadsContinued=True)}
            response = base_schema.build_response(request, kwargs)
            self.write_message(response)

    def generate_StoppedEvent(self, reason, thread_id, all_threads_stopped=None, preserve_focus_hint=None):
        """
        Parameters
        ----------
        preserve_focus_hint:bool
        reason : str
            "step","breakpoint", "exception", "pause" or "entry"
        thread_id : int
        all_threads_stopped : bool
        """
        body = schema.StoppedEventBody(reason,
                                       description='Stopped with reason: ' + str(reason),
                                       threadId=thread_id,
                                       allThreadsStopped=all_threads_stopped,
                                       preserveFocusHint=preserve_focus_hint)
        event = schema.StoppedEvent(body)
        self.write_message(event)

    def generate_OutputEvent(self,
                             output,
                             category=None,
                             group=None,
                             variablesReference=None,
                             source=None,
                             line=None,
                             column=None,
                             data=None):
        """
        Parameters
        ----------
        output:str
            The output to report.
        category:str
            The output category. If not specified, 'console' is assumed.
            Values: 'console', 'stdout', 'stderr', 'telemetry', etc.
        group:str
            Support for keeping an output log organized by grouping related messages.

            'start': Start a new group in expanded mode. Subsequent output events are members of the group and should be
            shown indented.
            The 'output' attribute becomes the name of the group and is not indented.

            'startCollapsed': Start a new group in collapsed mode. Subsequent output events are members of the group and
             should be shown indented (as soon as the group is expanded).
            The 'output' attribute becomes the name of the group and is not indented.

            'end': End the current group and decreases the indentation of subsequent output events.
            A non empty 'output' attribute is shown as the unindented end of the group.

        variablesReference: int
            If an attribute 'variablesReference' exists and its value is > 0, the output contains objects which can be
            retrieved by passing 'variablesReference' to the 'variables' request. The value should be less than or equal
            to 2147483647 (2^31 - 1).
        source: schema.Source
            An optional source location where the output was produced.
        line: int
            An optional source location line where the output was produced.
        column: int
            An optional source location column where the output was produced.
        data:
            Optional data to report. For the 'telemetry' category the data will be sent to telemetry, for the other
            categories the data is shown in JSON format.

        """
        if not self.args.log_no_debug_console:
            body = schema.OutputEventBody(output=output,
                                          category=category,
                                          variablesReference=variablesReference,
                                          source=source,
                                          line=line,
                                          column=column,
                                          data=data)
            event = schema.OutputEvent(body)
            self.write_message(event)

    def generate_ContinuedEvent(self, thread_id, all_threads_continued=None):
        """
        Parameters
        ----------
        thread_id : int
        all_threads_continued : bool
        """
        body = schema.ContinuedEventBody(threadId=thread_id, allThreadsContinued=all_threads_continued)
        event = schema.ContinuedEvent(body)
        self.write_message(event)

    def generate_ThreadEvent(self, thread_id, reason='started'):
        """
        Parameters
        ----------
        thread_id : int
        reason : str
            "started" or "exited"
        """
        body = schema.ThreadEventBody(reason=reason, threadId=thread_id)
        event = schema.ThreadEvent(body=body)
        self.write_message(event)

    def on_threads_request(self, request):
        """
        Have own function, converting adapter threads -> list for a response body

        Parameters
        ----------
        request : schema.ThreadsRequest
        """
        def compose_list_for_body(adapter_threads):
            _thr_list = []
            for th in adapter_threads:
                id_from_gdb = th['id']
                func = str(th['frame']['func']).strip("?")
                if func:
                    name = "id - " + str(
                        id_from_gdb) + ", " "frame -" + th['frame']['func'] + ', ' 'targetID - ' + th['target-id']
                else:
                    name = "id - " + str(id_from_gdb) + ", " "frame on address: " + th['frame'][
                        'addr'] + ', ' 'targetID - ' + th['target-id']
                thread_obj = schema.Thread(int(id_from_gdb), name)
                _thr_list.append(thread_obj.to_dict())
            return _thr_list

        if self.da.args.developer_mode == DaDevModes.CON_CHECK:
            return
        # === working:
        try:
            thr_list = compose_list_for_body(self.da.get_thread_list())
            success = True  # type: bool
            message = None
            # kwargs = {'body': schema.ThreadsResponseBody(thr_list)}
        except Exception as e:
            thr_list = []
            success = False  # type: bool
            message = log.debug_exception(e)
            kwargs = {'body': None}

        kwargs = {'body': schema.ThreadsResponseBody(thr_list)}
        threads_response = base_schema.build_response(request, kwargs)
        threads_response.success = success
        threads_response.message = message
        self.write_message(threads_response)

    def on_stackTrace_request(self, request):
        """
        Parameters
        ----------
        request: schema.StackTraceRequest
        """
        success = True
        try:
            # reading:
            thread_id = request.arguments.threadId
            stack = self.da.get_backtrace(thread_id)
            # composing
            stack_frames_list = []  # type: list[schema.StackFrame]
            for frame in stack:
                src = schema.Source(path=get_good_path(frame.get('fullname')))
                try:
                    line = int(frame.get('line'))
                except TypeError:
                    line = None
                if not str(frame.get('func')).strip('?'):
                    name = frame.get('addr')
                else:
                    name = frame.get('func')
                sf = schema.StackFrame(
                    id=self.da.frame_id_generate(thread_id, frame['level']),
                    name=name,
                    line=line,
                    column=0,
                    source=src,
                    instructionPointerReference=frame.get('addr')
                )
                stack_frames_list.append(sf.to_dict())  # to_dict because of a json encoding error
            kwargs = {
                'body': schema.StackTraceResponseBody(stackFrames=stack_frames_list, totalFrames=len(stack_frames_list))
            }
        except Exception as e:
            success = False  # type: bool
            log.debug_exception(e)
            kwargs = {'body': schema.ErrorResponseBody(e)}
        response = base_schema.build_response(request, kwargs)
        response.success = success
        self.write_message(response)

    def on_scopes_request(self, request):
        """
        Parameters
        ----------
        request:schema.ScopesRequest
        """
        frame_id = request.arguments.frameId
        success = True
        try:
            self.da.select_frame(frame_id)
            scopes_for_body = []  # type: list[schema.Scope]
            scopes = self.da.get_scopes()
            for scope in scopes:
                scope_dap_obj = schema.Scope(name=scope['name'],
                                             variablesReference=int(scope['var_ref']),
                                             expensive=False,
                                             presentationHint=scope['p_hint'])
                scopes_for_body.append(scope_dap_obj.to_dict())
            # building a response:
            kwargs = {'body': schema.ScopesResponseBody(scopes=scopes_for_body)}
        except Exception as e:
            success = False
            log.debug_exception(e)
            kwargs = {'body': schema.ErrorResponseBody(e)}
        response = base_schema.build_response(request, kwargs)
        response.success = success
        self.write_message(response)

    def on_source_request(self, request):
        src_file_path = get_good_path(request.arguments.source.path)
        success = True
        try:
            with open(src_file_path) as file:
                src = file.read()
        except Exception as e:
            src = "[UNKNOWN SOURCE FILE]\n---------------------"
            log.debug_exception(e)
            success = False
        response = base_schema.build_response(request, kwargs={'body': {'content': src}})  # type: schema.Source
        response.success = success
        self.write_message(response)

    def on_setVariable_request(self, request):
        """
        Parameters
        ----------
        request:schema.SetVariableRequest
        """
        if self.da.args.postmortem:
            response = base_schema.build_response(request)
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            name = request.arguments.name
            value = request.arguments.value
            self.da.set_variable(name, value)
            response = base_schema.build_response(request, kwargs={'body': {
                'value': value
            }})  # type: schema.SetVariableResponse
            self.write_message(response)

    def on_readMemory_request(self, request):
        """
        Parameters
        ----------
        request: schema.ReadMemoryRequest
        """
        if self.da.args.postmortem:
            response = base_schema.build_response(request)
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent("Not implemented")
        else:
            # TO DO GET COUNT of variable or DEFINE amount of bytes to read from memory
            try:
                memory_bytes = self.da.read_memory(request.arguments.memoryReference, 4000, request.arguments.offset)
                kwargs = {'body': schema.ReadMemoryResponseBody(request.arguments.memoryReference, data=memory_bytes)}
                response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ReadMemoryResponse
                response.success = True
            except Exception as e:
                log.debug_exception(e)
                kwargs = {'body': schema.ErrorResponseBody(e)}
                response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
                response.success = False
            self.write_message(response)

    def on_evaluate_request(self, request):
        """
        Parameters
        ----------
        request: schema.EvaluateRequest

        """
        expression = request.arguments.expression
        try:
            frame_id = request.arguments.frameId
        except AttributeError:
            frame_id = None
        self.da.select_frame(frame_id)
        # on_evaluate_request can execute gdb command if the evaluation expression started with `-exec`
        if len(expression) > 6 and expression[:6] == "-exec ":
            cmd_output = ''

            def get_output(type, stream, output):
                nonlocal cmd_output
                cmd_output += output

            self.da._gdb.stream_handler_add('console', get_output)
            self.da.gdb_execute(expression[6:])
            evaluate_response = base_schema.build_response(
                request, kwargs={'body': {
                    'result': cmd_output.replace("\\n", "\n"),
                    'variablesReference': 0
                }})

        # if the expression did't start with  `-exec` do the evaluate command
        elif request.arguments.context == "watch":
            result = self.da.evaluateVariable(expression)
            kwargs = {'body': schema.EvaluateResponseBody(
                str(result['value']), result['ref'], memoryReference=result['mem_addr'])}
            evaluate_response = base_schema.build_response(request, kwargs)
        else:
            result = self.da.evaluate(expression)  # no symbol and other errors processing
            evaluate_response = base_schema.build_response(
                request, kwargs={'body': {
                    'result': str(result),
                    'variablesReference': 0
                }})
        self.write_message(evaluate_response)
        self.generate_OutputEvent(output="WARNING! This feature can't update UI after execution.", category="console")

    def on_setExpression_request(self, request):
        """
        Parameters
        ----------
        request:schema.SetExpressionRequest
        """
        kwargs = {}
        response = base_schema.build_response(request, kwargs)
        self.write_message(response)

    def on_dataBreakpointInfo_request(self, request):
        """
        Parameters
        ----------
        request:schema.DataBreakpointInfoRequest
        """
        varRef = request.arguments.variablesReference
        name = request.arguments.name
        access_type = ['read', 'write', 'readWrite']
        kwargs = {'body': schema.DataBreakpointInfoResponseBody(
            dataId=varRef, description=name, accessTypes=access_type, canPersist=True)}
        response = base_schema.build_response(request, kwargs)
        self.write_message(response)

    def on_setDataBreakpoints_request(self, request):
        """
        Parameters
        ----------
        request:schema.SetDataBreakpointsRequest
        """
        data_bps = request.arguments.breakpoints  # type: list[dict]
        self.da.data_break_removeall()

        success = True
        for bp in data_bps:
            access_type = bp['accessType']
            expr = bp['description']
            try:
                self.da.data_break_add(expr, access_type)
            except Exception as e:
                bp.update({'verified': 'false'})
                bp.update({{'message': e}})
                log.debug_exception(e)
                break

        kwargs = {'body': schema.SetDataBreakpointsResponseBody(data_bps)}
        response = base_schema.build_response(request, kwargs)
        response.success = success
        self.write_message(response)

    def on_variables_request(self, request):
        """
        Parameters
        ----------
        request:schema.VariablesRequest
        """
        self.evaluated = False
        variables_for_body = []  # type: list[schema.Variable]
        try:
            da_vars = self.da.get_vars(request.arguments.variablesReference)
            for v in da_vars:
                v_dap_obj = schema.Variable(name=v['name'],
                                            value=v['value'],
                                            variablesReference=v['ref'],
                                            memoryReference=v['mem_addr'])
                variables_for_body.append(v_dap_obj.to_dict())
            kwargs = {'body': schema.VariablesResponseBody(variables=variables_for_body)}
            response = base_schema.build_response(request, kwargs)
            self.write_message(response)
        except Exception as e:
            log.debug_exception(e)
            kwargs = {'body': schema.ErrorResponseBody(e)}
            response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
            response.success = False
            self.write_message(response)

    def on_disconnect_request(self, request):
        """
        Parameters
        ----------
        request:schema.DisconnectRequest
        """
        try:
            # reading
            r_args = request.arguments.to_dict()
            restart = r_args.get('restart')
            # doing
            disconnect_response = base_schema.build_response(request)
            self.generate_OutputEvent("Debug Adapter stopped\n")
            self.da.adapter_stop()
            self.write_message(disconnect_response)
            if restart:
                self.da.adapter_restart()
        except Exception as e:
            log.debug_exception(e)
            kwargs = {'body': schema.ErrorResponseBody(e)}
            response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
            response.success = False
            self.write_message(response)

    def on_pause_request(self, request):
        """
        Parameters
        ----------
        request:schema.PauseRequest
        """
        response = base_schema.build_response(request)
        if self.da.args.postmortem:
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            try:
                thread_id = request.arguments.threadId
                self.da.pause()
                self.write_message(response)
                self.generate_StoppedEvent(reason='pause', thread_id=int(thread_id), all_threads_stopped=True)
            except Exception as e:
                log.debug_exception(e)
                kwargs = {'body': schema.ErrorResponseBody(e)}
                response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
                response.success = False
                self.write_message(response)

    def generate_BreakpointEvent(self, reason, bp):
        """
        Parameters
        ----------
        reason : str
            The reason for the event.
        bp: schema.Breakpoint
            breakpoint: The breakpoint.
        """
        body = schema.BreakpointEventBody(reason, bp)
        event = schema.BreakpointEvent(body)
        self.write_message(event)

    def on_setBreakpoints_request(self, request):
        """
        Parameters
        ----------
        request: schems.SetBreakpointsRequest
        """
        def try_set_once(source_path, line, condition):
            try:
                return self.da.source_break_add(source_path, line, condition=condition)
            except Exception as e:
                raise e

        kwargs = {'body': schema.SetBreakpointsResponseBody([])}
        success = False
        if self.da.args.postmortem:
            response = base_schema.build_response(request, kwargs)
            response.success = success
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            bps = request.arguments.breakpoints  # type: list[dict]
            source = request.arguments.source
            self.da.source_break_removeall(source.path)  # clear old ones

            for bp in bps:
                src_line = bp.get('line')
                condition = bp.get("condition", '')
                log_message = bp.get('logMessage', '')
                bp.update({'verified': 'true'})
                bp.update({'source': source.to_dict()})
                try_count = 5
                while try_count:
                    try_count -= 1
                    try:
                        if log_message:
                            self.da.source_logpoint_add(get_good_path(source.path), src_line, log_message, condition)
                            self.generate_OutputEvent(log_message + "\n")
                        else:
                            try_set_once(get_good_path(source.path), src_line, condition)
                        kwargs = {'body': schema.SetBreakpointsResponseBody(bps)}
                        success = True
                        break
                    except Exception as e:
                        bp.update({'verified': 'false'})
                        bp.update({{'message': e}})
                        log.debug_exception(e)

            response = base_schema.build_response(request, kwargs)
            response.success = success
            self.write_message(response)

    def on_setExceptionBreakpoints_request(self, request):
        """
        Parameters
        ----------
        request:schema.SetExceptionBreakpointsRequest
        """
        response = base_schema.build_response(request)
        if self.da.args.postmortem:
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            self.write_message(response)

    def on_next_request(self, request):
        """
        Parameters
        ----------
        request:schema.NextRequest
        """
        m = Measurement()
        thread_id = request.arguments.threadId

        response = base_schema.build_response(request)
        if self.da.args.postmortem:
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)

        else:
            try:
                result = self.da.step()
                response.success = result
                self.write_message(response)
                if result:
                    self.generate_StoppedEvent(reason='step', thread_id=thread_id, all_threads_stopped=True)
                m.stop_n_check(0.5, "The step operation took too long")
            except Exception as e:
                log.debug_exception(e)
                kwargs = {'body': schema.ErrorResponseBody(e)}
                response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
                response.success = False
                self.write_message(response)

    def on_stepIn_request(self, request):
        """
        Parameters
        ----------
        request:schema.StepInRequest
        """

        response = base_schema.build_response(request)
        if self.da.args.postmortem:
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            try:
                thread_id = request.arguments.threadId
                result = self.da.step_in()
                response.success = result
                self.write_message(response)
                if result:
                    self.generate_StoppedEvent(reason='step', thread_id=thread_id, all_threads_stopped=True)
            except Exception as e:
                log.debug_exception(e)
                kwargs = {'body': schema.ErrorResponseBody(e)}
                response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
                response.success = False
                self.write_message(response)

    def on_stepOut_request(self, request):
        """
        Parameters
        ----------
        request:schema.StepOutRequest
        """

        response = base_schema.build_response(request)
        if self.da.args.postmortem:
            response.success = False
            self.write_message(response)
            self.generate_OutputEvent(POST_MORTEM_MODE_NOTIFICATION)
        else:
            try:
                thread_id = request.arguments.threadId
                result = self.da.step_out()
                response.success = result
                if result:
                    self.generate_StoppedEvent(reason='step', thread_id=thread_id, all_threads_stopped=True)
                self.write_message(response)
            except Exception as e:
                log.debug_exception(e)
                kwargs = {'body': schema.ErrorResponseBody(e)}
                response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
                response.success = False
                self.write_message(response)

    def on_disassemble_request(self, request):
        """
        Parameters
        ----------
        request : schema.DisassembleRequest
        """
        end_addr = int(request.arguments.memoryReference, 16) + \
            request.arguments.instructionCount + request.arguments.instructionOffset
        try:
            data, errors = self.da.get_disassemble_instructions(request.arguments.memoryReference, hex(end_addr))
            kwargs = {'body': schema.DisassembleResponseBody(instructions=data)}
            response = base_schema.build_response(request, kwargs)  # type: schema.DisassembleResponse
            response.body.address = request.arguments.memoryReference
            response.body.unreadableBytes = errors
            response.success = True
            self.write_message(response)
        except Exception as e:
            log.debug_exception(e)
            kwargs = {'body': schema.ErrorResponseBody(e)}
            response = base_schema.build_response(request, kwargs=kwargs)  # type: schema.ErrorResponse
            response.success = False
            self.write_message(response)

    def on_setInstructionBreakpoints_request(self, request):
        """
        Parameters
        ----------
        request : schema.SetInstructionBreakpointsRequest
        """
        ibps = request.arguments.breakpoints  # type: list[dict]
        for ibp in ibps:
            try:
                self.da.inst_break_add(ibp.get('instructionReference'), '')
            except Exception as e:
                ibp.update({'verified': 'false'})
                ibp.update({{'message': e}})
                log.debug_exception(e)
        kwargs = {'body': schema.SetInstructionBreakpointsResponseBody(breakpoints=request.arguments.breakpoints)}
        response = base_schema.build_response(request, kwargs)
        response.success = True
        self.write_message(response)

    def write_message(self, protocol_message):
        """
        Some instance of one of the messages in the debug_adapter.schema.

        Parameters
        ----------
        protocol_message:Type(schema.Response)
        """
        self.write_queue.put(protocol_message)
