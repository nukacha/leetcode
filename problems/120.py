from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                min_child = min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )
                triangle[i][j] += min_child
        return triangle[0][0]
