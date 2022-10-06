#!/usr/bin/python3
""" Module square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor method, inherit from rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def __str__(self):
        """ return the data of the square """
        x = f"[Square] ({self.id}) "
        y = f"{self.x}/{self.y} - {self.__size}/{self.__size}"
        return x + y
