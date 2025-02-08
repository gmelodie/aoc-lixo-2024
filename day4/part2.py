import numpy as np
import sys

matrix = []
for line in sys.stdin:
    matrix.append([x for x in line.strip()])

matrix = np.array(matrix)

check_matrices = [
    [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]],
    [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]],
    [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
    [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]],
]


def check_sub_matrix(matrix, checker):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if (checker[i, j] != ".") and (matrix[i, j] != checker[i, j]):
                return False
    return True


count = 0
for i in range(len(matrix) - 2):
    for j in range(len(matrix[0]) - 2):
        sub_matrix = matrix[i:i + 3, j:j + 3]
        for checker in check_matrices:
            if check_sub_matrix(sub_matrix, np.array(checker)):
                count += 1

print(count)
