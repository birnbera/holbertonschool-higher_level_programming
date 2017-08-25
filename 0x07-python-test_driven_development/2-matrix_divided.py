#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Function to divide all elements of `matrix` by `div`

    Args:
        matrix: 2d array (list of lists) of integers/floats.
        div: Divisor of `matrix`. Must be either integer or float.

    Returns:
        New matrix with result of the division of each element of
        `matrix` by `div`.

    Raises:
        TypeError: If `matrix` not 2d or contains non-int/float
            elements or `div` is neither an integer nor float.
            Also if `matrix` is ragged (not all rows of equal length).
        ZeroDivisionError: If `div` is 0.
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    types_row = map(lambda x: type(x) is list, matrix)
    if not all(types_row):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        types_element = map(lambda x: type(x) is float or type(x) is int,
                            row)
        if not all(types_element):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
    sizes = map(lambda x: len(x) == len(matrix[0]), matrix)
    if not all(sizes):
        raise TypeError('Each row of the matrix must have the same size')

    mat_div = list(map(lambda x:
                       list(map(lambda y:
                                round(y / div, 2), x)), matrix))
    return mat_div
