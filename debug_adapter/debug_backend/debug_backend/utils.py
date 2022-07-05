import os

from .defs import NoGdbProcessError

# This function needs to be called for paths passed to OOCD or GDB commands.
# API handles this automatically but ut should be used when if user composes commands himself, e.g. for Gdb.monitor_run().
# It makes paths portable across Windows and Linux versions of the tools.
def fixup_path(path):
    file_path = path
    if os.name == 'nt':
        # Convert filepath from Windows format if needed
        file_path = file_path.replace("\\","/");
    return file_path


def verify_valid_gdb_subprocess(gdb_process):
    """Verify there is a process object, and that it is still running.
    Raise NoGdbProcessError if either of the above are not true."""
    if not gdb_process:
        raise NoGdbProcessError("gdb process is not attached")

    elif gdb_process.poll() is not None:
        raise NoGdbProcessError(
            "gdb process has already finished with return code: %s"
            % str(gdb_process.poll())
        )