#!/usr/bin/python3
"""Read File Function"""


def read_file(filename=""):
    """Read File Function"""
    with open(filename, 'r') as pr:
        print(pr.read(), end="")
