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
    a = int(a)
    b = int(b)
    return (a+b)
