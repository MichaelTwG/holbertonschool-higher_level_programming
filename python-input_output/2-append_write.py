#!/usr/bin/python3
""" Module append_write"""


def write_file(filename="", text=""):
    """ append in filename the text"""
    with open(filename, "a") as File:
        return File.write(text)
