#!/usr/bin/python3
def no_c(my_string):
    lst = []
    for char in my_string:
        lst.append(char)
    for i in range(0, len(lst)):
        if lst[i] == 'C' or lst[i] == 'c':
            lst[i] == ''
    return ''.join(lst)
