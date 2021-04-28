import os
import pathlib

HERE = pathlib.Path(__file__).parent
test_app_srcs = [
    HERE / "host" / "test_app.c",
    HERE / "host" / "test_app_src2.c"
]
test_app_out = HERE / "host" / "test_app"

os.system("gcc -O0 -g -pthread %s -o %s" % (' '.join(str(e) for e in test_app_srcs), str(test_app_out)))
