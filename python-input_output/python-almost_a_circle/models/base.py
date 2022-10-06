#!/usr/bin/python3
""" Module class Base """


class Base:
    """ This clase is the base of all clases in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects
