#!/usr/bin/python3
"""
    Count number of lines in a file
"""


def number_of_lines(filename=""):
    """
        Count number of lines in a file
    """
    count = 0
    with open(filename) as num:
        for count, l in enumerate(num, start = 1):
            pass
    return count
