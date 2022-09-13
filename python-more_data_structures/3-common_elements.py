#!/usr/bin/python3
from distutils.log import set_threshold


def common_elements(set_1, set_2):
    set_res = []
    for x in sorted(set_1):
        for y in sorted(set_2):
            if (x == y):
                set_res.append(x)
    return set(set_res)
