#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary2 = a_dictionary.copy()
    for key, value in a_dictionary2.items():
        a_dictionary2[key] = value * 2
    return a_dictionary2
