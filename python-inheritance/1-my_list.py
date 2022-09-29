#!/usr/bin/python3
""" Module My Print """


class MyList(list):
    """
        Class MyList - inherits from list
            Megthod: print_sorted: print the list, in acending sort
    """
    def print_sorted(self):
        """ print list in acending order """
        print(sorted(self))
