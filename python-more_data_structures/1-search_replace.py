#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = my_list[:]
    for i in range(0, cp.count(search)):
        cp[cp.index(search)] = replace
    return cp
