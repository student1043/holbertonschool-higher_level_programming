#!/usr/bin/python3
class MyInt(int):
    """Def MyInt"""
    def __eq__(self, other):
        """Returning !="""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Returning =="""
        return int.__eq__(self, other)
