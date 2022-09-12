#!/usr/bin/python3
def no_c(my_string):
    cp_list = []
    for char in my_string:
         cp_list.append(char)
    for i in range(0, len(cp_list)):
        if cp_list[i] == 'C' or cp_list[i] == 'c':
            cp_list[i] = ''
    return ''.join(cp_list)
