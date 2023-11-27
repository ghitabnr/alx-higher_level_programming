#!/usr/bin/python3


import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """Solve the N queens puzzle using backtracking"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve_col(board, col, N):
        if col >= N:
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve_col(board, col + 1, N)
                board[row][col] = 0

    solve_col(board, 0, N)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
