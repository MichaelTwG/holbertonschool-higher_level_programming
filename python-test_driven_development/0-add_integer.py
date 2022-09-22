#!/usr/bin/python3
"""
    this function add two ints or floats
"""


def add_integer(a, b=98):
    """add_integer add a and b"""
    if type(a) != float and type(a) != int:
        print("a must be an integer")
    if type(b) != float and type(b) != int:
        print("b must be an integer")
    if type(b) == float:
        b = int(b)
    if type(a) == float:
        a = int(a)
    if a is not None and b is not None:
        return (a+b)
