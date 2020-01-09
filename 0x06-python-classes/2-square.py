#!/usr/bin/python3
class Square:
    """This is a square class"""
    def __init__(self, size=0):
        """This is a definition"""
        self.__size = size
        """This is an attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
