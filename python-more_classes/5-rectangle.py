#!/usr/bin/python3
""" Module rectangle.py - create a class called Rectangle"""


class Rectangle:
    """
        The clase Rectangle
            Args:
                Width (int)
                Height (int)
    """
    def __init__(self, width=0, height=0):
        """ Constructor method for the class Rectangle, this code is ejecuted
        when an new istnace is created
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        string_return = ""

        if self.__height == 0 or self.__width == 0:
            return string_return
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string_return += "#"
            if i < self.__height - 1:
                string_return += "\n"
        return string_return

    def __print__(self):
        print(self.__str__)

    def __repr__(self):
        width = str(self.__width)
        heigth = str(self.__height)

        return "Rectangle(" + width + ", " + heigth + ")"

    def __del__(self):
        print("Bye rectangle...")
