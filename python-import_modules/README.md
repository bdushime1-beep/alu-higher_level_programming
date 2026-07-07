# 0x02. Python - import & modules

## Description

This project covers Python imports and modules: importing functions
and variables from other files, using command-line arguments (`sys.argv`),
and inspecting compiled `.pyc` modules.

It is part of the ALU Higher Level Programming curriculum.

## Repository

- **GitHub repository:** `alu-higher_level_programming`
- **Directory:** `python-import_modules`

## Requirements

- All scripts interpreted/compiled on Ubuntu 20.04 LTS
- All Python files: first line must be `#!/usr/bin/python3`
- All files must end with a new line
- All Python files must be executable (`chmod +x filename`)
- Code should follow the pycodestyle style guide (version 2.8.*)
- Code should not execute when imported (`if __name__ == "__main__":`)

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-add.py` | Imports `add` from `add_0.py`, prints `1 + 2 = 3` |
| 1 | `1-calculation.py` | Imports functions from `calculator_1.py`, prints add/sub/mul/div results |
| 2 | `2-args.py` | Prints the number and list of command-line arguments |
| 3 | `3-infinite_add.py` | Prints the sum of all command-line arguments |
| 4 | `4-hidden_discovery.py` | Prints all public names defined in `hidden_4.pyc` |
| 5 | `5-variable_load.py` | Imports and prints the variable `a` from `variable_load_5.py` |

## Usage

```bash
./0-add.py
./1-calculation.py
./2-args.py Hello Welcome
./3-infinite_add.py 79 10
./4-hidden_discovery.py
./5-variable_load.py
```

## Author

Your Name
