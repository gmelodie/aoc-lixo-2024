import numpy as np
import sys

matrix = []
for line in sys.stdin:
    matrix.append([x for x in line.strip()])

matrix = np.array(matrix)


def horizontal_xmas(matrix):
    count = 0

    for line in matrix:
        str_line = "".join(line)
        count += str_line.count("XMAS")
        count += str_line.count("XMAS"[::-1])

    return count


def vertical_xmas(matrix):
    return horizontal_xmas(matrix.T)


def diagonal_xmas(matrix):
    count = 0
    rows, cols = matrix.shape
    positive_diagonals = []

    for d in range(-rows + 1, cols):
        positive_diagonals.append(list(np.diagonal(matrix, offset=d)))

    count += horizontal_xmas(positive_diagonals)

    negative_diagonals = []
    flipped_lr_matrix = np.fliplr(matrix)
    for d in range(-rows + 1, cols):
        negative_diagonals.append(list(np.diagonal(flipped_lr_matrix, offset=d)))

    count += horizontal_xmas(negative_diagonals)

    return count


count = horizontal_xmas(matrix) + vertical_xmas(matrix) + diagonal_xmas(matrix)
print(count)
