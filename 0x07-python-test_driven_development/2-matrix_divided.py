#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix

    Parameters:
        matrix(int): the matrix list
        div(int): integer that divides elements in matrix

    Return:
        a new matrix
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(error_msg)
    if not isinstance(matrix, list):
        raise TypeError(error_msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for num in matrix:
        if (len(matrix[0]) != len(num)):
            raise TypeError("Each row of the matrix must have the same size")
        for item in num:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(error_msg)

    return [[round(item / div, 2) for item in num] for num in matrix]
