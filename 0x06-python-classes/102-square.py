#!/usr/bin/python3
class Square:
    """This is a square class"""
    def __init__(self, size=0):
        """This is a definition"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This will return area of square"""
        return (self.__size*self.__size)

    @property
    def size(self):
        """This is a definition"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is a definition"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __eq__(self, other):
        """This is a definition"""
        return self.__size == other.__size

    def __ne__(self, other):
        """This is a definition"""
        return self.__size != other.__size

    def __lt__(self, other):
        """This is a definition"""
        return self.__size < other.__size

    def __le__(self, other):
        """This is a definition"""
        return self.__size <= other.__size

    def __gt__(self, other):
        """This is a definition"""
        return self.__size > other.__size

    def __ge__(self, other):
        """This is a definition"""
        return self.__size >= other.__size
