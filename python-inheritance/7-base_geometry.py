#!/usr/bin/python3
""" This module create a new class BaseGeometry"""


class BaseGeometry:
    """
        BaseGeometry class
            Methods:
                area ()
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
