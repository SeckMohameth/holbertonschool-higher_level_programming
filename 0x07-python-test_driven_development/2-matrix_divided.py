#!/usr/bin/python3
""" a function that divides
 all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """divide elements in matrix

    Args:
    matrix: list in a list
    div: int or float dividing byt

    Returns:
    Nothing

    Raises:
    TypeError: matrix must be a 27 matrix (list of lists) of integers/floats

    TypeError: div must be a number

    ZeroDivisionError: division by zero

    """


    new_list = []
    second_list = []


    for eachList in matrix:
        for eachNumber in matrix:
            if not len(eachList)  len(matrix[0]):
                raise TypeError("Each row of the matrix must have the\
 same size")
                second_list.append(eachNumber/div)
        new_list.append(second_list)
        second_list = []


        if float not in matrix and int not in matrix:
            raise TypeError("matrix must be a matrix (list of\
            lists) of integers/floats")

        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

    return new_list
