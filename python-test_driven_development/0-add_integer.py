#!/usr/bin/python3
"""
    this function add two ints or floats
"""


def add_integer(a, b=98):
    """add_integer add a and b"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(a) is not int:
        raise TypeError("b must be an integer")
    return (a+b)
