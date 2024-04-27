#!/usr/bin/python3 

def pascal_triangle(n):
    """ that returns a list of lists of integers representing the Pascal’s triangle of n """
    if type(n) != int or n < 0:
        raise ValueError("Input must be nonnegative integer.")
    result = []
    for i in range(n+1):                   
        result.append([])             
        result[i].extend([1]*(i+1))        
        if i > 0:                                                    
            for j in range(len(result[i-1])):       
                result[i][j] += result[i-1][j]              
    return result
print(pascal_triangle(4))
