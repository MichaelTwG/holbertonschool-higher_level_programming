#!/usr/bin/python3
"""
    module Rectangle
"""


class Rectangle:
    """ rectangle class """

    print_symbol = "#"
    number_of_instances = 0

    def __intit__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perimeter = (self.__width * 2) + (self.__height * 2)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        buf = ""

        if self.width == 0 or self.height == 0:
            return buf
        for i in range(self.height):
            for j in range(self.width):
                buf += str(self.print_simbol)
            if i != self.height - 1:
                buf += "\n"
        return buf

    def __repr__(self):
        w = str(self.width)
        h = str(self.height)

        return ("Rectangle(" + w + ", " + h + ")")

    def __del__(self):
        print("Bye rectangle...")
        Retangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an istance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an istance of Rectangle")

        if rect_1.area >= rect_2.area:
            return rect_1
        else:
            return rect_2

        @classmethod
        def square(cls, size=0):

            square_1 = Rectangle(size, size)
            return square_1
