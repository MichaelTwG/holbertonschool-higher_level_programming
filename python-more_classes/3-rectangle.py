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

    def area(self):
        """ return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter of the rectangle """
        perimeter = (self.__width * 2) + (self.__height * 2)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """ retrieves an informal string representation of a rectangle """
        buf = ""

        if self.width == 0 or self.height == 0:
            return buf
        for i in range(self.height):
            for j in range(self.width):
                buf += str(self.print_simbol)
            if i != self.height - 1:
                buf += "\n"
        return buf
