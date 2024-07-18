#!/usr/bin/python3

"""n x n 2D matrix, rotate it 90 degrees clockwise """


# function rotate matrix
def rotate_2d_matrix(matrix):
    n = len(matrix)
    # loop for rows && colomuns
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the rows
    for row in matrix:
        row.reverse()
