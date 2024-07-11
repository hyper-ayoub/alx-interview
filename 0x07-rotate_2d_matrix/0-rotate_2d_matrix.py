"""Rotate an n x n 2D matrix 90 degrees clockwise."""


# Function to rotate the matrix
def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Step 1: Transpose the matrix by swapping rows with columns
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()
