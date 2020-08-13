import os
import sys
import unittest
from xmlrunner import XMLTestRunner

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
try:
    import test_arguments
except ImportError:
    print("Can't import test_arguments")
    sys.exit(1)

# Make it possible to run this file from the root dir of DA without
# installing DA; useful for Travis testing, etc.
sys.path[0:0] = ['.']


def main():
    if not os.path.isfile('run_tests.py'):
        os.chdir(SCRIPT_DIR)
    runner = XMLTestRunner(verbosity=2, output='results')
    tests = unittest.TestSuite()
    tests.addTest(test_arguments.ArgumentsTest())
    result = runner.run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


if __name__ == '__main__':
    sys.exit(main())
