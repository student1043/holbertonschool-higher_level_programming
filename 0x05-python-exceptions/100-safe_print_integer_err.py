#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
            return(True)
        except (ValueError, TypeError):
            return(False)
            sys.stderr.write("Unknown format code 'd' for object of type 'str'")
    else:
        return(False)
