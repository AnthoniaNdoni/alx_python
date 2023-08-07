#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        squared_row = [x**2 for x in row]
        square_matrix.append(squared_row)
    return square_matrix