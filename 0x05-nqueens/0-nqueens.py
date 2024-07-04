#!/usr/bin/python3

""" n-queens """

import sys


def solve_nqueens(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    
    res = []
    board = [["."] * n for _ in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"
            
            backtrack(r + 1)
            
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."
    
    backtrack(0)
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        formatted_solution = []
        for r in range(N):
            for c in range(N):
                if solution[r][c] == "Q":
                    formatted_solution.append([r, c])
        print(formatted_solution)

if __name__ == "__main__":
    main()
