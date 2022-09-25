#!/usr/bin/python3
"""
    module print_square
"""


def print_square(size):
    """
        this function print a square with the character #
    """
    if type(size) is not int:
        raise TypeError("isize must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
