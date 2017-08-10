#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        return [[i**2 for i in row] for row in matrix]
