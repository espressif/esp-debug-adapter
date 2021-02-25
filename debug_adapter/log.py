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

from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, Formatter, FileHandler, Logger, StreamHandler, NOTSET
from .internal_classes import DaArgs
import os
import sys
import threading
from typing import Any

# CONFIG: **************************************************************************************************************

CFG_NO_DEBUG_CONSOLE = False
CGF_LOG_TO_MULT_FILES = False
CFG_BACKUP_OLD_LOG = False
CFG_LOG_FORMAT = '%(asctime)-15s - %(name)s - %(levelname)s - %(message)s'

# .CONFIG **************************************************************************************************************
formatter = None
stream_handler = None
file_handler = None
level = DEBUG
args = None  # type: DaArgs
__da = None  # placeholder for debug adapter instance. Need for avoiding circular imports
start_time = None  # type: Any[str, None]
_top_logger = None  # type: Any[Logger, None]
argval2loglevel = {0: CRITICAL, 1: ERROR, 2: WARNING, 3: INFO, 4: DEBUG}


def da():
    global __da
    return __da


class DebugAdapterLogger(Logger):
    def __init__(self, name, level=NOTSET, da_inst=None, with_console_output=True):
        """
        Parameters
        ----------
        name : str
            Name of the logger
        level : int
            Log level
        da_inst
            Debug adapter instance
        with_console_output : bool
            Print to debug console of VSCode
        """
        super(DebugAdapterLogger, self).__init__(name=name, level=level)
        self.con_out = with_console_output
        self.__da = da_inst

    def critical(self, msg, *args, **kwargs):
        if (not CFG_NO_DEBUG_CONSOLE) and self.con_out and da() and self.isEnabledFor(CRITICAL):
            da().output(msg)
        super(DebugAdapterLogger, self).critical(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        if (not CFG_NO_DEBUG_CONSOLE) and self.con_out and da() and self.isEnabledFor(WARNING):
            da().output(msg)
        super(DebugAdapterLogger, self).warning(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        if (not CFG_NO_DEBUG_CONSOLE) and self.con_out and da():
            da().output(msg)
        super(DebugAdapterLogger, self).exception(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        if (not CFG_NO_DEBUG_CONSOLE) and self.con_out and da() and self.isEnabledFor(ERROR):
            da().output(msg)
        super(DebugAdapterLogger, self).error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        if (not CFG_NO_DEBUG_CONSOLE) and self.con_out and da() and self.isEnabledFor(INFO):
            da().output(msg)
        super(DebugAdapterLogger, self).info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        if (not CFG_NO_DEBUG_CONSOLE) and self.con_out and da() and self.isEnabledFor(DEBUG):
            da().output(msg)
        super(DebugAdapterLogger, self).debug(msg, *args, **kwargs)

    def warning_no_con(self, msg, *args, **kwargs):
        super(DebugAdapterLogger, self).warning(msg, *args, **kwargs)

    def error_no_con(self, msg, *args, **kwargs):
        super(DebugAdapterLogger, self).error(msg, *args, **kwargs)

    def info_no_con(self, msg, *args, **kwargs):
        super(DebugAdapterLogger, self).info(msg, *args, **kwargs)

    def debug_no_con(self, msg, *args, **kwargs):
        super(DebugAdapterLogger, self).debug(msg, *args, **kwargs)

    def exception_no_con(self, msg, *args, **kwargs):
        super(DebugAdapterLogger, self).exception(msg, *args, **kwargs)


def getLogger(name=None, with_console_output=True):
    return DebugAdapterLogger(name, with_console_output=with_console_output)


def init(in_args,
         start_time_str='',
         add_to_file_name='',
         da_inst=None,
         backup_old_log=CFG_BACKUP_OLD_LOG,
         no_debug_console=False):
    err_msg = None
    global CGF_LOG_TO_MULT_FILES
    global formatter
    global stream_handler
    global file_handler
    global level
    global args
    global _top_logger
    global start_time
    global __da
    args = in_args
    start_time = start_time_str
    __da = da_inst
    level = argval2loglevel.get(args.debug, DEBUG)

    if args.log_mult_files:
        CGF_LOG_TO_MULT_FILES = True
    formatter = Formatter(CFG_LOG_FORMAT)
    stream_handler = StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    pref = ''
    if args.log_file is not None:
        try:
            if os.path.isfile(args.log_file) and backup_old_log:  # if old log file exists
                st = ""
                with open(args.log_file) as f:
                    first_line = f.readline()
                    st_mark = first_line[-31:-20]
                    if st_mark == 'START_TIME_':
                        st = first_line[-20:-1]
                if st:
                    path_a, path_b = os.path.split(args.log_file)
                    path_b = st + "_" + path_b
                    renamed_path = os.path.join(path_a, path_b)
                    os.rename(args.log_file, renamed_path)
        except Exception as e:
            err_msg = e

        file_handler = FileHandler(pref + args.log_file, 'w')
        file_handler.setFormatter(formatter)
    else:
        file_handler = None
    _top_logger = new_logger(log_name='Debug Adapter (main)',
                             stream_handler_=stream_handler,
                             file_handler_=file_handler,
                             with_console_output=(not args.log_no_debug_console))
    debug_no_con("START_TIME_" + start_time)
    debug_no_con("Init errors:" + str(err_msg))


def new_logger(log_name='Logger',
               logging_level_=None,
               stream_handler_=None,
               file_handler_=None,
               with_console_output=True):
    """

    Parameters
    ----------
    log_name : str
    logging_level_ : int
    stream_handler_ : StreamHandler
    file_handler_ : FileHandler
    with_console_output :bool

    Returns
    -------

    """
    global CGF_LOG_TO_MULT_FILES
    logger = getLogger(log_name, with_console_output=with_console_output)
    if logging_level_:
        logger.setLevel(logging_level_)
    else:
        global level
        logger.setLevel(level)
    if stream_handler_:
        logger.addHandler(stream_handler_)
    else:
        global stream_handler
        logger.addHandler(stream_handler)
    if file_handler_:
        if CGF_LOG_TO_MULT_FILES:
            file_handler_ = get_file_handler(log_name)
        else:
            file_handler_ = get_file_handler()
        logger.addHandler(file_handler_)
    else:
        global file_handler  # check if global file_handler is defined
        if file_handler:
            if CGF_LOG_TO_MULT_FILES:
                file_handler_mult = get_file_handler(log_name)
                logger.addHandler(file_handler_mult)
            else:
                logger.addHandler(file_handler)
    logger.propagate = False
    return logger


def get_file_handler(file_pref=''):
    if not file_pref:
        global file_handler
        return file_handler
    else:
        global start_time
        file_pref = file_pref \
            .replace(" ", "_") \
            .lower()
        if len(start_time):
            file_pref = str(start_time) + '_' + file_pref
        folder, filename = os.path.split(args.log_file)
        filepath = os.path.join(folder, file_pref + filename)
        fh = FileHandler(filepath, 'w')
        fh.setFormatter(formatter)
        return fh


_debug_lock = threading.Lock()
#
# strings
dbg_msg_empty = "debug_exception without any message"
dbg_msg_convert_error = "DEBUG OUTPUT ERROR: debug_exception(msg) got msg which can not to handle"


def dbg_msg_to_str(msg):
    if msg:  # if there is some message
        if type(msg) is not str:
            # TODO: processing of non str
            try:
                msg_str = str(msg) + '\n'
            except TypeError:
                msg_str = dbg_msg_convert_error
            return msg_str
        else:
            return msg
    else:
        return dbg_msg_empty


def debug(msg):
    _top_logger.debug(msg)


def debug_no_con(msg):
    _top_logger.debug_no_con(msg)


def info(msg):
    _top_logger.info(msg)


def info_no_con(msg):
    _top_logger.info_no_con(msg)


def warning(msg):
    _top_logger.warning(msg)


def warning_no_con(msg):
    _top_logger.warning_no_con(msg)


def cmd(msg):
    _top_logger.critical(msg)


def cmd_no_con(msg):
    _top_logger.critical_no_con(msg)


def log(msg, level):
    _top_logger.log(level, msg)


def debug_exception(msg=None):
    if not msg:
        import traceback
        traceback.print_exc()
    else:
        _top_logger.exception(msg)


def debug_exception_no_con(msg=None):
    if not msg:
        import traceback
        traceback.print_exc()
    else:
        _top_logger.exception_no_con(msg)


level = DEBUG
formatter = Formatter(CFG_LOG_FORMAT)
stream_handler = StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
_top_logger = new_logger(log_name='early Debug Adapter (main)',
                         stream_handler_=stream_handler,
                         file_handler_=file_handler)
