#!/usr/bin/python3
""" Module square """
from multiprocessing.sharedctypes import Value
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor method, inherit from rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        super(Square, type(self)).width.fset(self, value)
        super(Square, type(self)).height.fset(self, value)

    def __str__(self):
        """ return the data of the square """
        x = f"[Square] ({self.id}) "
        y = f"{self.x}/{self.y} - {self.size}"
        return x + y
    
    def update(self, *args, **kwargs):
        """ update the class atributes using kwars """
        if args and len(args) > 0:
            if len(args) >= 2:
                args_1 = (args[0], args[1])
                args_2 = args_1 + args[1:]
                args = args_2
        else:
            if 'size' in kwargs.keys():
                kwargs['width'] = kwargs.pop('size')
                kwargs['height'] = kwargs['width']
        super(Square, self).update(*args, **kwargs)
