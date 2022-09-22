#!/usr/bin/python3
"""
    Create a class called Square
"""


class Square:
    """ Atribute: size (int): private size of the square """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiation Variables: Size """
        self.__size = size
        self.__position = position

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
    def position(self, position=(0, 0)):
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for x in range(0, self.__position[0]):
                print()
            for i in range(0, self.size):
                for x in range(0, self.__position[1]):
                    print(" ", end="")
                for i in range(0, self.size):
                    print("#", end="")
                print()
