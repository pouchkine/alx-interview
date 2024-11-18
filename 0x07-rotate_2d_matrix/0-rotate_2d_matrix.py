#!/usr/bin/python3
"""
inverse of a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """body of the fonction
    """
    n_col = len(matrix[0])
    matrix.reverse()
    matrix = [[ligne[i] for ligne in matrix] for i in range(n_col)]
