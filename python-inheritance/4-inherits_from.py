#!/usr/bin/python3
""" Module inherits_from """


def inherits_from(obj, a_class):
    """ check if obj inherits of the a_class """

    if not (type(obj) == a_class) and isinstance(obj, a_class):
        return True
    else:
        return False
