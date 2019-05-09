#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    neo = []
    morpheus = []
    for each_list in matrix:
        for each_number in each_list:
            morpheus.append(each_number**2)
        neo.append(morpheus)
        morpheus = []
    return neo
