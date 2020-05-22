from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [0] * (i + 1)
            row[0] = row[-1] = 1
            for j in range(1, i):
                row[j] = sum(triangle[i - 1][j - 1:j + 1])
            triangle.append(row)
        return triangle
