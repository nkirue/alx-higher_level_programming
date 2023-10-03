#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_bard(n):
    """ This initialize the of sized chessboard ."""
    bard = []
    [bard.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in bard]
    return (bard)


def bard_deepcopy(bard):
    """deepcopy of a chessboard."""
    if isinstance(bard, list):
        return list(map(bard_deepcopy, bard))
    return (bard)


def get_slution(bard):
    """the list of lists representa of a solved chessboard."""
    slution = []
    for e in range(len(bard)):
        for c in range(len(bard)):
            if bard[r][c] == "Q":
                slution.append([e, c])
                break
    return (slution)


def xut(bard, row, col):
    """X out spots on a chessboard. """
    # X out 
    for c in range(col + 1, len(bard)):
        bard[row][c] = "x"
    # X out backwards
    for c in range(col - 1, -1, -1):
        bard[row][c] = "x"
    # X out spots below
    for r in range(row + 1, len(bard)):
        bard[r][col] = "x"
    # X out spots above
    for r in range(row - 1, -1, -1):
        bard[r][col] = "x"
    # X out diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(bard)):
        if c >= len(bard):
            break
        bard[r][c] = "x"
        c += 1
    # X out  diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        bard[r][c]
        c -= 1
    # X out diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(bard):
            break
        bard[r][c] = "x"
        c += 1
    # X out diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(bard)):
        if c < 0:
            break
        bard[r][c] = "x"
        c -= 1


def recursive_slve(bard, row, queens, slutions):
    """this recursively solve an N-queens puzzle."""
    if queens == len(bard):
        slutions.append(get_slution(bard))
        return (slutions)

    for c in range(len(bard)):
        if bard[row][c] == " ":
            tmp_bard = bard_deepcopy(bard)
            tmp_bard[row][c] = "Q"
            xout(tmp_bard, row, c)
            slutions = recursive_slve(tmp_bard, row + 1,
                                        queens + 1, slutions)

    return (slutions)

#print N
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bard = init_bard(int(sys.argv[1]))
    slutions = recursive_slve(bard, 0, 0, [])
    for sl in slutions:
        print(sl)
