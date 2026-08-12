#!/usr/bin/python3
"""Solve the N queens puzzle."""

import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at row and col."""
    for previous_row in range(row):
        previous_col = board[previous_row][1]

        if previous_col == col:
            return False

        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve(board, row, n):
    """Find and print all solutions using backtracking."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve(board, row + 1, n)
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve([], 0, n)
