#!/usr/bin/python3
""" Module Square inherit from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """ 
        Class Rectangle
            Args:   size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size