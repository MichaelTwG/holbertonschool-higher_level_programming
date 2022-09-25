#!/usr/bin/python3
"""
    Module text_indentation
"""


def text_indentation(text):
    """
        Print text with new indentation
    """
    result = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] in {'.', ':', '?'}:
            result += text[i]
            result += "\n\n"
        else:
            result += text[i]
    for i in range(0, len(result)):
        if result[i] == " " and result[i - 1] == "\n" and i != 0:
            pass
        else:
            print(result[i], end="")
