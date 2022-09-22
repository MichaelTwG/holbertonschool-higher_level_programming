#!/usr/bin/python3
"""
    Create a class called Square
"""


class Square:
    """ Atribute: size (int): private size of the square """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiation Variables: Size """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for x in range(0, self.__position[1]):
                print()
            for i in range(0, self.size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.size):
                    print("#", end="")
                print()
