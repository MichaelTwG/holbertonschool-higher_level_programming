#!/usr/bin/python3
import string


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
