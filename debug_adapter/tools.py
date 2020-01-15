import os
import sys
import time
from datetime import datetime
from . import log

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2
WIN32 = sys.platform == "win32"

if WIN32:
    import win32api


class ObjFromDict(object):
    """
    @DynamicAttrs
    Turns a dictionary into a class
    """

    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __repr__(self):
        """"""
        return "<FromDict: %s>" % str(self.__dict__)

    def get_dict(self):
        return self.__dict__


def path_disassemble(in_path):
    """

    Parameters
    ----------
    in_path: str

    Returns
    -------
    win_drive: str
    path: str
    name: str
    extension: str
    exists: bool
    """
    path_abs = os.path.abspath(in_path)

    win_drive, tail = os.path.splitdrive(path_abs)
    path, f_ext = os.path.split(tail)
    name, extension = os.path.splitext(f_ext)
    exists = os.path.exists(path_abs)
    return win_drive, path, name, extension, exists


def get_good_path(srs_path):
    """

    Parameters
    ----------
    srs_path

    Returns
    -------
    srs_path
    """
    r = ""
    try:
        if not WIN32:
            r = str(srs_path)
        else:
            r = win32api.GetLongPathName(win32api.GetShortPathName(srs_path))
    except Exception as e:
        r = srs_path
    return r


class Measurement(object):
    def __init__(self):
        self.start = time.time()  # type: float
        self.end = None  # type: float
        self.time = None  # type: float

    def _ending(self):
        self.end = time.time()
        self.time = self.end - self.start

    def _logging(self, level):
        log.log("Measured %f s ( from ~ %s)" % (
            self.time,
            datetime.fromtimestamp(self.start).strftime("%H:%M:%S,%f")
        ), level)

    def _warning(self, warn_msg):
        log.warning("%s - Measured %f s ( from ~ %s)" % (
            warn_msg,
            self.time,
            datetime.fromtimestamp(self.start).strftime("%H:%M:%S,%f")))

    def stop(self):
        self._ending()
        self._logging(log.INFO)

    def stop_n_check(self, warn_time_thr, warn_msg="The operation took too long!"):
        """

        Parameters
        ----------
        warn_time_thr : float
            in seconds
        warn_msg : str
            in words

        Returns
        -------

        """
        self._ending()
        if self.time > warn_time_thr:
            self._warning(warn_msg)
            return True
        return False
