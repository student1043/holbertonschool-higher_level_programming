#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ This is class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is def init """
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is not None:
            self.id = id

        @property
        def width(self):
            """ width property """
            return self.__width

        @width.setter
        def width(self, value):
            """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

        @property
        def height(self):
            """ height property """
            return self.__height

        @height.setter
        def height(self, value):
            """ height setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

        @property
        def x(self):
            """ x property """
            return self.__x

        @x.setter
        def x(self, value):
            """ x setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__x = value

        @property
        def y(self):
            """ y property """
            return self.__y

        @y.setter
        def y(self, value):
            """ y setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__y = value
