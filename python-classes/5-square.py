#!/usr/bin/python3
"""
    Create a class called Square
"""


class Square:
    """ Atribute: size (int): private size of the square """

    def __init__(self, size=0):
        """ Instantiation Variables: Size """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(0, len(self.size)):
            for i in range(0, len(self.size)):
                print("#", end="")
            print()
