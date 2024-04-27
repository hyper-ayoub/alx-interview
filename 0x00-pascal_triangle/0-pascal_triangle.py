#!/usr/bin/python3
"""
Pass in a number n and return a list of lists representing the first n rows of Pascal's Triangle.
"""

def pascal_triangle(n):
    """Pass in a number n and return a list of lists representing the first n rows
    of Pascal's Triangle."""
    triangle = []
    if n > 0:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
    return triangle
