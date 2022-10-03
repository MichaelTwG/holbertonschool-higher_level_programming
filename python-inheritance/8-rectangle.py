#!/usr/bin/python3
""" Module Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class rectangle:
            Width
            Height
    """
    def __init__(self, width, height):
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__heigth = height
