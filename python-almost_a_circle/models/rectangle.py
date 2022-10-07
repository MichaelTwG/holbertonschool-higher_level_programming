#!/usr/bin/python3
""" Module Rectangle"""
from typing import Type
from models.base import Base


class Rectangle(Base):
    """ Define a rectangle and inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ display a rectangle in stdout"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ return the data of the rectangle """
        x = f"[Rectangle] ({self.id}) "
        y = f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return x + y

    def update(self, *args, **kwargs):
        """ update the class atributes using kwars"""
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "width" in kwargs.keys():
                self.__width = kwargs["width"]
            if "height" in kwargs.keys():
                self.__height = kwargs["height"]
            if "x" in kwargs.keys():
                self.__x = kwargs["x"]
            if "y" in kwargs.keys():
                self.__y = kwargs["y"]

    def to_dictionary(self):
        return vars(self)
