#!/usr/bin/python3
""" Module 9-rectangle - Create a class called Square """


class Rectangle:
    """ Rectangle class defined by width and height """

    print_symbol = "#"
    number_of_instances = 0

    def __intit__(self, width=0, height=0):
        """Constructor method, initizlizes a rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @propery
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
