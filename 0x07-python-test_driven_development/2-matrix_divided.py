#!/usr/bin/python3
"""Module containing function to divide 2d matrix elementwise.

Not directly executable, but can be imported.
"""


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
        OverflowError: If `matrix` contains '+/-inf' or 'nan'.
    """
    if not isinstance(div, (float, int)) or div != div:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    types_row = map(lambda x: isinstance(x, list), matrix)
    if not all(types_row):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        types_element = map(lambda x: isinstance(x, (float, int)), row)
        if not all(types_element):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
    for row in matrix:
        types_element = map(lambda x: x == x
                            and x != float('inf')
                            and x != -float('inf'),
                            row)
        if not all(types_element):
            raise OverflowError
    sizes = map(lambda x: len(x) == len(matrix[0]), matrix)
    if not all(sizes):
        raise TypeError('Each row of the matrix must have the same size')

    mat_div = list(map(lambda x:
                       list(map(lambda y:
                                round(y / div, 2), x)), matrix))
    return mat_div
