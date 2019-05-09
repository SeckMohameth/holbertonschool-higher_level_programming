#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    newList = []
    for each_list in matrix:
        for each_number in each_list:
            newList.append(each_number**2)
        newMatrix.append(newList)
        newList = []
    return newMatrix
