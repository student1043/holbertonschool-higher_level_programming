#!/usr/bin/python3
"""
    Read n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """
        Read n lines of a text file
    """
    with open(filename, 'r') as pr:
        for i in range(nb_lines):
            line = pr.readline()
            print(line, end="")
        if nb_lines <= 0 or nb_lines >= len(list(pr)):
            for i in pr:
                print(i, end="")
