import sys
import os
from .gdb import Gdb
from .oocd import Oocd
from .hw_specific import *


def get_hw_list():
    hw_list = []
    p = os.path.dirname(__file__)
    files = os.listdir(os.path.join(p, "hw_specific"))
    for f in files:
        hw_list.append(os.path.splitext(f)[0])
    return hw_list


def _str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def get_gdb(chip_name=None,
            gdb_path=None,
            log_level=None,
            log_stream_handler=None,
            log_file_handler=None,
            log_gdb_proc_file=None,
            remote_target=None,
            remote_address=None,
            remote_port=None, **kwargs):
    """
    set to != None value to redefine get_gdb logic

    Parameters
    ----------
    chip_name : Any(None, str)
    gdb_path : Any(None, str)
    log_level : Any(None, str)
    log_stream_handler : Any(None, str)
    log_file_handler : Any(None, str)
    log_gdb_proc_file : Any(None, str)
    remote_target : Any(None, str)
    remote_address : Any(None, str)
    remote_port : Any(None, str)

    Returns
    -------
    Gdb
    """
    if chip_name in get_hw_list():
        _gdb = _str_to_class("Gdb" + chip_name)
    else:
        _gdb = Gdb

    return _gdb(gdb_path=gdb_path,
                log_level=log_level,
                log_stream_handler=log_stream_handler,
                log_file_handler=log_file_handler,
                log_gdb_proc_file=log_gdb_proc_file,
                remote_target=remote_target,
                remote_address=remote_address,
                remote_port=remote_port, **kwargs)


def get_oocd(chip_name=None,
             oocd_exec=None,
             oocd_scripts=None,
             oocd_args=None,
             ip=None,
             log_level=None,
             log_stream_handler=None,
             log_file_handler=None,
             **kwargs):
    """
    set to != None value to redefine get_gdb logic

    Parameters
    ----------
    chip_name : Any(None, str)
    oocd_exec : Any(None, str)
    oocd_scripts : Any(None, str)
    oocd_args : Any(None, str)
    ip : Any(None, str)
    log_level : Any(None, str)
    log_stream_handler : Any(None, str)
    log_file_handler : Any(None, str)

    Returns
    -------
    Any
    """
    if chip_name in get_hw_list():
        _oocd = _str_to_class("Oocd" + chip_name)
    else:
        _oocd = Oocd
    return _oocd(chip_name=chip_name,
                 oocd_exec=oocd_exec,
                 oocd_scripts=oocd_scripts,
                 oocd_args=oocd_args,
                 ip=ip,
                 log_level=log_level,
                 log_stream_handler=log_stream_handler,
                 log_file_handler=log_file_handler, **kwargs)
