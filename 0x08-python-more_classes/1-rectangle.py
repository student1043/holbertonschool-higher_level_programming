#!/usr/bin/python3
class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Init Def for width and height"""
        self.__height = height
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Definition Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Definition Width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Definition Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Definition Height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
