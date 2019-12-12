#!/usr/bin/python3
num = 0

if __name__ == "__main__":
    import sys
    for i in range(1, len(sys.argv)):
        num += int(sys.argv[i])
    print("{}".format(num))
