#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    int_list = []
    try:
        for i in range(0, x):
            print("{:d}".format(mi_list[i]), end="")
            int_list.append(mi_list[i])
            count += 1
        print()
    except (IndexError, ValueError, TypeError):
        pass
