#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" Module Square inherit from Rectangle"""


class Square(Rectangle):
    """ 
        Class Rectangle
            Args:   size
    """
    def __inint__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size