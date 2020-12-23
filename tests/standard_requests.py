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

from debug_adapter import schema

REQUEST_INIT = schema.Request(command="initialize",
                              arguments={
                                  "adapterID": "espidf",
                                  "clientID": "vscode",
                                  "clientName": "Visual Studio Code",
                                  "columnsStartAt1": True,
                                  "linesStartAt1": True,
                                  "locale": "en-us",
                                  "pathFormat": "path",
                                  "supportsRunInTerminalRequest": True,
                                  "supportsVariablePaging": True,
                                  "supportsVariableType": True
                              })

REQUEST_LAUNCH = schema.Request(command="launch",
                                arguments={
                                    "__sessionId": "79b3673d-5b08-44e5-98ca-429a521464cb",
                                    "externalConsole": False,
                                    "logging": {
                                        "engineLogging": True
                                    },
                                    "name": "Launch",
                                    "preLaunchTask": "adapter",
                                    "request": "launch",
                                    "type": "espidf"
                                })
