#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for num in list(set(my_list)):
        res += num
    return res
