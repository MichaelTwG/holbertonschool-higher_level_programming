#!/usr/bin/python3
''' Module is_kinf_of_class '''


def is_kind_of_class(obj, a_class):
    """
        check if is obj an istance of the class a_class or
        an instance of a class that inherited from
    """
    return isinstance(obj, a_class)
