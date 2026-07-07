# 0x01. Python - if/else, loops, functions

## Description

This project covers conditional statements, loops, and functions in
Python. It builds on basic Python syntax to introduce control flow
(`if`/`elif`/`else`), iteration (`for`/`while`), and reusable functions,
including manipulating ASCII values and writing simple algorithms like
FizzBuzz.

It is part of the ALU Higher Level Programming curriculum.

## Repository

- **GitHub repository:** `alu-higher_level_programming`
- **Directory:** `python-if_else_loops_functions`

## Requirements

- All scripts interpreted/compiled on Ubuntu 20.04 LTS
- All Python files: first line must be `#!/usr/bin/python3`
- All files must end with a new line
- All Python files must be executable (`chmod +x filename`)
- Code should follow the pycodestyle style guide (version 2.8.*)
- Unless otherwise noted, you are not allowed to import any module
- All functions must have a docstring / all files must have a module
  docstring (tested with `python3 -c 'print(__import__("module").__doc__)'`)

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-positive_or_negative.py` | Prints whether a random number is positive, negative, or zero |
| 1 | `1-last_digit.py` | Prints the last digit of a random number, with a description of its value |
| 2 | `2-print_alphabet.py` | Prints the lowercase ASCII alphabet using one loop and one print |
| 3 | `3-print_alphabt.py` | Prints the lowercase ASCII alphabet, excluding `q` and `e` |
| 4 | `4-print_hexa.py` | Prints numbers 0 to 98 in decimal and hexadecimal |
| 5 | `5-print_comb2.py` | Prints numbers 00 to 99, comma-separated |
| 6 | `6-print_comb3.py` | Prints all smallest two-digit combinations of two different digits |
| 7 | `7-islower.py` | Function `islower(c)` — checks if a character is lowercase |
| 8 | `8-uppercase.py` | Function `uppercase(str)` — prints a string in uppercase |
| 9 | `9-print_last_digit.py` | Function `print_last_digit(number)` — prints and returns the last digit |
| 10 | `10-add.py` | Function `add(a, b)` — returns the sum of two integers |
| 11 | `11-pow.py` | Function `pow(a, b)` — returns `a` to the power of `b` |
| 12 | `12-fizzbuzz.py` | Function `fizzbuzz()` — prints numbers 1-100, replacing multiples of 3/5 with Fizz/Buzz/FizzBuzz |

## Usage

Each script can be run directly from the command line:

```bash
./0-positive_or_negative.py
./1-last_digit.py
./2-print_alphabet.py
./3-print_alphabt.py
./4-print_hexa.py
./5-print_comb2.py
./6-print_comb3.py
```

Function-based files (7 onward) are meant to be imported and tested via
a corresponding `*-main.py` test file, e.g.:

```bash
./7-main.py
./8-main.py
./9-main.py
./10-main.py
./11-main.py
./12-main.py
```

Make sure scripts are executable:

```bash
chmod +x *.py
```

## Author

Your Name
