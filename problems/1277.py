from itertools import chain
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        for i in range(1, n_row):
            for k in range(1, n_col):
                if matrix[i][k]:
                    matrix[i][k] += min(
                        matrix[i - 1][k],
                        matrix[i][k - 1],
                        matrix[i - 1][k - 1])
        return sum(chain(*matrix))
