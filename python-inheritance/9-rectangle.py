#!/usr/bin/python3
""" Module Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class rectangle:
            Width
            Height
        Methds:
            area
            print
            str
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ return the aria of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] <{self.__width}>/<{self.__height}>"
