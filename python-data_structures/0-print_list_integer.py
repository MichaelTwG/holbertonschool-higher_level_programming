#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if (my_list != None):
        for i in range(0, len(my_list)):
            print("{:d}".format(my_list[i]))
