#!/usr/bin/python3 
# Pascal Triangle -> alx interview  question

def pascal_triangle(n):
    """ that returns a list of lists of integers representing the Pascal’s triangle of n """

    if type(n) != int or n < 0:
        raise ValueError("Input must be nonnegative integer.")
    result = []
    for i in range(n+1):                   # Loop through each line (row).
        result.append([])                   # Start new sublist for this line.
        result[i].extend([1]*(i+1))         # Fill with ones, then zeros.
        if i > 0:                                                     # Not on first line?
            for j in range(len(result[i-1])):       # Copy previous line's values.
                result[i][j] += result[i-1][j]               # Add next value from prev.
    return result

print(pascal_triangle(4))
