#!/usr/bin/python3
"""
    Module add_integer
"""


def add_integer(a, b=98):
    """
        add_integer: adds two integers, a and b
        Return: the result or exception msg
    """

    if (a is None or (not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
