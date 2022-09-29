#!/usr/bin/python3
""" Module My Print """


class MyList(list):
    """
        Class MyList - inherits from list
            Megthod: print_sorted: print the list, in acending sort
    """
    def print_sorted(self):
        """ print list in acending order """
        list_sorted = sorted(self)
        print(list_sorted)
        return list_sorted
