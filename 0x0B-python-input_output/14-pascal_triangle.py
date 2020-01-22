#!/usr/bin/python3
"""
    Pascal Triangle
"""


def pascal_triangle(n):
    """
        Pascal Triangle
    """
    list = []
    if n <= 0:
        return list
    for n in range(1, n + 1):
        list.append(1)

        for i in range(n - 2, 0, -1):
            list[i] += list[i - 1]
            return list[i]
