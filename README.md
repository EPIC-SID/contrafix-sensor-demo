# Sensor Average: ContraFix Bug Demo

A deliberately broken, small Python project for a debugging demo.
The failing tests are intentional. This is not a production sensor library.

## The Bug Report

Our sensor dashboard crashes when a sensor does not send a reading.
A missing reading is represented by `None` and should be ignored.
Zero and negative numbers are real readings and must still count.
When every reading is missing, or the list is empty, return `None`.

| Readings | Expected average |
| --- | --- |
| `10, 20, 30` | `20` |
| `10, missing, 20` | `15` |
| `0, 10, missing` | `5` |
| `0, 0, missing` | `0` |
| `-10, 0, missing` | `-5` |
| Only missing readings | `None` |
| Empty list | `None` |

## Run Locally

Use Python 3.10 or newer. From this repository's directory:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
```

On macOS/Linux, replace `.\.venv\Scripts\python.exe` with `.venv/bin/python`.

The starting version should produce **2 passing and 5 failing tests**.
A correct fix should pass all **7 tests** without modifying the tests.

## Use in ContraFix

1. Import this public repository URL.
2. Choose `solution.py` as the source file.
3. Choose existing tests and select `test_solution.py` as the test file.
4. Paste the bug report below and save your selection.

```text
The sensor dashboard crashes when readings contain None. Ignore missing
readings, but keep zero and negative numbers. Return None if there are no
actual readings. Fix average_reading without changing its name or the tests.
```

ContraFix currently supports read-only GitHub import and selection. Executing
imported repositories remains disabled until an isolated runner is available.
Importing this demo does not bypass that safety gate or automatically fix it.
The built-in average-reading example can demonstrate actual test execution today.

## Demo Goal

Compare a proposed fix with an independent review, then check the complete
test suite. A fix must preserve existing behavior as well as stop the crash.
The repository contains no model keys, external services, package setup scripts,
or hidden correct solution. Runtime dependencies use Python's standard library.
