#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ This is class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is def init """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ width property """
            return self.__width

        @property
        def height(self):
            """ height property """
            return self.__height

        @property
        def x(self):
            """ x property """
            return self.__x

        @property
        def y(self):
            """ y property """
            return self.__y

        @width.setter
        def width(self, value):
            """ width setter """
            self.__width = value

        @height.setter
        def height(self, value):
            """ height setter """
            self.__height = value

        @x.setter
        def x(self, value):
            """ x setter """
            self.__x = value

        @y.setter
        def y(self, value):
            """ y setter """
            self.__y = value
