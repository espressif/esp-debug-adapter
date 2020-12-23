# Copyright (c) Microsoft Corporation. All rights reserved.
# Additions Copyright (c) 2020, Espressif Systems (Shanghai) Co. Ltd.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, division, print_function, unicode_literals

import py
import pytest
import sys
import threading
from debugpy.common import compat


@pytest.fixture
def daemon(request):
    """Provides a factory function for daemon threads. The returned thread is
    started immediately, and it must not be alive by the time the test returns.
    """

    daemons = []

    def factory(func, name_suffix=""):
        name = func.__name__ + name_suffix
        thread = threading.Thread(target=func, name=name)
        thread.daemon = True
        daemons.append(thread)
        thread.start()
        return thread

    yield factory

    try:
        failed = request.node.call_report.failed
    except AttributeError:
        pass
    else:
        if not failed:
            for thread in daemons:
                assert not thread.is_alive()


if sys.platform != "win32":

    @pytest.fixture
    def long_tmpdir(request, tmpdir):
        return tmpdir


else:
    import ctypes

    GetLongPathNameW = ctypes.windll.kernel32.GetLongPathNameW
    GetLongPathNameW.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32]
    GetLongPathNameW.restype = ctypes.c_uint32

    @pytest.fixture
    def long_tmpdir(request, tmpdir):
        """Like tmpdir, but ensures that it's a long rather than short filename on Win32.
        """
        path = compat.filename(tmpdir.strpath)
        buffer = ctypes.create_unicode_buffer(512)
        if GetLongPathNameW(path, buffer, len(buffer)):
            path = buffer.value
        return py.path.local(path)
