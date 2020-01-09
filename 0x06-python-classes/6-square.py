#!/usr/bin/python3
class Square:
    """This is a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """This is a definition"""
        self.__size = size
        self.__postition = position
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

    @property
    def position(self):
        """This is a definition"""
        return self.__postition

    @position.setter
    def position(self, value):
        """This is a definition"""
        self.__postition = value()
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """This is a definition"""
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
        if self.__postition[1] > 0:
            print()
        else:
            print(" ")
