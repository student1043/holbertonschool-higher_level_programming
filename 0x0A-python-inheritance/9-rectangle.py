#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """ Initit """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
    def area(self):
        """Area Def"""
        return (self.__height * self.__width)
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
