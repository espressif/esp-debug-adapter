import os
import pathlib

HERE = pathlib.Path(__file__).parent
test_app_src = HERE / "host" / "test_app.c"
test_app_out = HERE / "host" / "test_app"

os.system("gcc -O0 -g %s -o %s" % (str(test_app_src), str(test_app_out)))
