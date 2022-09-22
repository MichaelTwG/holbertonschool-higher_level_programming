#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) != float or type(a) != int:
        print("a must be an integer")
    if type(b) != float or type(b) != int:
        print("b must be an integer")
    a = int(a)
    b = int(b)
    return (a+b)
