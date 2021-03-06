#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ This is class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is def init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Area of the Rectangle """
        return(self.__width * self.__height)

    def display(self):
        """ Display Rectangle Instance """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ string """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update with args """
        num = 0
        if args != ():
            for f in args:
                num += 1
                if num == 1:
                    self.id = f
                if num == 2:
                    self.width = f
                if num == 3:
                    self.height = f
                if num == 4:
                    self.x = f
                if num == 5:
                    self.y = f
        else:
            for i, j in kwargs.items():
                if i == "width":
                    self.width = j
                if i == "height":
                    self.height = j
                if i == "id":
                    self.id = j
                if i == "x":
                    self.x = j
                if i == "y":
                    self.y = j

    def to_dictionary(self):
        """ dictionary """
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height,
                "width": self.width}
