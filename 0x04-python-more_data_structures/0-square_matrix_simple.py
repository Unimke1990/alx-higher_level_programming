#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_rows = []
        for elements in row:
            new_rows.append(elements**2)
        new_matrix.append(new_rows)
    return new_matrix
