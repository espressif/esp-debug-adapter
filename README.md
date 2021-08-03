# esp_debug_adapter

esp_debug_adapter works as connecting part between IDE and an Debug server. From the IDE side it is needed to follow [DAP](https://microsoft.github.io/debug-adapter-protocol/), from Debug server this adapter is compatible with [GDB/MI](https://www.sourceware.org/gdb/onlinedocs/gdb/GDB_002fMI.html) protocol.

Table of Content:

*   [Usage](#Usage)
*   [References](#References)

See also:

*   [Start Modes and Arguments](docs/start_modes_and_arguments.md)
*   [Testing](docs/testing.md)
*   [Auto-generated documentation](docs/src/doxygen.md)

## Usage

For advanced arguments description follow to specific section: [Start Modes and Arguments](docs/start_modes_and_arguments.md)

Basic description is bellow:

```bash
Usage: debug_adapter_main.py [OPTIONS]

Options:
  -a, --app_flash_off INTEGER     Program start address offset
                                  (ESP32_APP_FLASH_OFF)  [default: 65536]
  -b, --board-type TEXT           Type of the board to run tests on (you could
                                  use OOCD_TEST_BOARD envvar by default)
  -d, --debug INTEGER             Debug level (0-4), 5 - for a full OOCD log
                                  [default: 2]
  -dn, --device-name TEXT         The name of used hardware to debug
                                  (currently Esp32 or Esp32_S2). It defines
                                  --toolchain-prefix
  -p, --port INTEGER              Listen on given port for VS Code connections
                                  [default: 43474]
  -pm, --postmortem               Run the adapter without target in 'read-
                                  only' mode
  --developer-mode [none|connection-check|x86-test]
                                  Modes for development purposes  [default:
                                  none]
  -l, --log-file TEXT             Path to log file.
  -lm, --log-mult-files           Log to separated files
  -t, --toolchain-prefix TEXT     (If not set, controlled by --device-name!)
                                  Toolchain prefix. If set, rewrites the value
                                  specified by --device-name.
  -e, --elfpath TEXT              A path to elf files for debugging. You can
                                  use several elf files e.g. `-e file1.elf -e
                                  file2.elf`
  -c, --core-file TEXT            Use a file as a core dump to examine.
  -x, --cmdfile TEXT              Path to a command file containing commands
                                  to automatic execute during a program
                                  startup
  -tsf, --tmo-scale-factor        Scale factor for gdb timeout [default:1]
  -o, --oocd TEXT                 Path to OpenOCD binary file, (used
                                  OPENOCD_BIN envvar or (if not set) 'openocd'
                                  by default)  [default: openocd]
  -oa, --oocd-args TEXT           (If not set, drives by --device-name!)
                                  Specifies custom OpenOCD args. If set,
                                  rewrites the value specified by --device-
                                  name.
  -om, --oocd-mode [run_and_connect|connect_to_instance|without_oocd]
                                  Cooperation with OpenOCD  [default:
                                  connect_to_instance]
  -ip, --oocd-ip TEXT             Ip for remote OpenOCD connection  [default:
                                  localhost]
  -s, --oocd-scripts TEXT         Path to OpenOCD TCL scripts (use
                                  OPENOCD_SCRIPTS envvar by default)
  --help                          Show this message and exit.
```



## References

*   This software used at the Espressif's vscode-plugin, but could be run standalone

*   The project contains debug adapter written in python following  a protocol my Microsoft https://microsoft.github.io/debug-adapter-protocol/


## Credits and licensing

This software is based on a [tutorial](https://github.com/fabioz/python_debug_adapter_tutorial) by Fabio Zadrozny.

All original code in this repository is Copyright 2020 Espressif Systems (Shanghai) Co. Ltd.

The project is released under Eclipse Public License 2.0.

In case an individual source file is also available under a different license, this is indicated in the file itself.
