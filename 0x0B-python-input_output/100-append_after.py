#!/usr/bin/python3
"""
    Search and Replace
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Search and Replace
    """
    with open(filename, "r") as pr1:
        while True:
            list = []
            line = pr1.readline()
            if line == "":
                break
            list.append(line)
            if search_string in line:
                list.append(new_string)
    with open(filename, "w") as pr:
        pr.writelines(list)
