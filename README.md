# Python Scripts Repository

This repository contains a set of simple Python scripts each demonstrating some basic and common operations in Python. 

## Table of Contents
- [File Input & Output](#file-input--output)
- [User Input](#user-input)
- [Regular Expressions](#regular-expressions)
- [Custom Python Modules & Functions](#custom-python-modules--functions)
- [Array of Procedures & JSON](#array-of-procedures--json)

## File Input & Output

The `file_io.py` script provides a good example of basic file I/O operations in Python. 

**How to Run:**
```shell
python file_io.py
```

## User Input

The `user_input.py` script provides basic examples to handle command-line parameters as well as real-time input from a user.

**How to Run:**
```shell
python user_input.py
```

For a more complex handling of user input, you can check out `user_input_complex.py`. It provides an overview and examples of the features provided by the Python `argparse` module. 

**How to Run:**
```shell
python user_input_complex.py -h
```
Then, follow the provided help.

## Regular Expressions

The `regex_ohya.py` script provides a basic introduction to using regular expressions in Python. 

**How to Run:**
```shell
python regex_ohya.py
```

## Custom Python Modules & Functions

The `newmodule.py` script is a basic introduction to both custom modules and functions in Python. This script is not intended to be run via the command line.

To see how to access custom-built Python modules, you can run the `usemodule.py` script.

**How to Run:**
```shell
python usemodule.py
```

## Array of Procedures & JSON

The `steps.py` module contains a handful of functions, each intended to be a single step in a complex procedure.

The `run_procedure.py` script accepts a JSON file that specifies a module and an order of execution for functions, as well as the associated parameters. The module is loaded and functions are executed as specified by the JSON.

**How to Run:**
```shell
python run_procedure.py -h
```
Then, follow the directions provided.

Finally, the `build_json.py` script demonstrates how to turn a Python data structure into a JSON string and write that to disk. This script was used to build the JSON file that is the input for `run_procedure.py`.

Enjoy exploring these scripts and learning Python!
