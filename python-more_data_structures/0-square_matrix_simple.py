#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in range(0, len(matrix)):
        res.append(list(map(lambda x: x*x, matrix[i])))
    return res
