#!/usr/bin/python3
"""
MOCK INTERVIEW QUESTION
"""


def rotate_2d_matrix(mat):
    """
    Rotates a 2D matrix 90 degrees clockwise iN place
    """
    N = len(mat)

    for x in range(0, N // 2):
        for y in range(x, N - 1 - x):
            temp = mat[x][y]
            mat[x][y] = mat[N - 1 - y][x]
            mat[N - 1 - y][x] = mat[N - 1 - x][N - 1 - y]
            mat[N - 1 - x][N - 1 - y] = mat[y][N - 1 - x]
            mat[y][N - 1 - x] = temp
