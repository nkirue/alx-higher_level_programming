#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys

def is_saf(bard, row, col, n):
    # This check if a queen can be placed in the given cell (row, col)
    for i in range(col):
        if bard[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if bard[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if bard[i][j] == 1:
            return False

    return True

def slve_n_queens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    bard = [[0] * n for _ in range(n)]
    slutions = []
    
    def slve(col):
        if col == n:
            slutions.append(bard[:])
            return
        
        for row in range(n):
            if is_safe(bard, row, col, n):
                bard[row][col] = 1
                slve(col + 1)
                bard[row][col] = 0
    
    slve(0)
    
    for slution in slutions:
        for row in slution:
            print("".join(["Q" if cell == 1 else "." for cell in row]))
        print()

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

slve_n_queens(N)
