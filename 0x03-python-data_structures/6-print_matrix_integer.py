#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row[:-1]:
            print("{:d}".format(col), end=" ")
        if row:
            print("{:d}".format(row[-1]))
        else:
            print()
