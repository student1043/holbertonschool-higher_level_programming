#!/usr/bin/python3
class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        return (Rectangle(size, size))

    def __init__(self, width=0, height=0):
        """Init Def for width and height"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __repr__(self):
        """representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def area(self):
        """Definition"""
        return(self.__width*self.__height)

    def perimeter(self):
        """Definition"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(2*(self.__width + self.__height))

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

    def __str__(self):
        """This is a definition"""
        hit = ""
        for i in range(self.__height):
            for j in range(self.__width):
                hit += " ".join(Rectangle.print_symbol)

            if i != self.__height - 1:
                hit += " ".join("\n")
        if self.__width == 0 or self.__height == 0:
            return '\n'
        return hit

    def __del__(self):
        """This is a definition"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

        def bigger_or_equal(rect_1, rect_2):
            if type(rect_1) is not Rectangle:
                raise TypeError("rect_1 must be an instance of Rectangle")
            if type(rect_2) is not Rectangle:
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1.area() < rect_2.area():
                return (rect_2)
            else:
                return (rect_1)
