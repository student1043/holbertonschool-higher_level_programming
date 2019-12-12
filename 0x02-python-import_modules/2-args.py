#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) > 0:
        if len(sys.argv) - 1 == 1:
            print("{:d} argument:".format(len(sys.argv) - 1))
        elif len(sys.argv) == 1:
            print("0 arguments.")
        else:
            print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
