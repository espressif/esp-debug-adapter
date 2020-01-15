import sys
from pylint.pyreverse.main import Run

file = "../debug_adapter/__main__.py"
cmd_args = sys.argv  # save old args
pyrev_args = ['-o', 'pdf', '-p', 'uml', '-SA', file, '../debug_adapter']
sys.argv = [cmd_args[0]] + pyrev_args  # load args for pyreverse
Run(sys.argv)