#!/usr/bin/python3
import sys
num = 0
if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        num += int(sys.argv[i])
    print(num)
