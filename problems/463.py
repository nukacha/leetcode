from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimiter = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                perimiter += i == 0 or grid[i - 1][j] == 0
                perimiter += i == len(grid) - 1 or grid[i + 1][j] == 0
                perimiter += j == 0 or row[j - 1] == 0
                perimiter += j == len(row) - 1 or row[j + 1] == 0
        return perimiter
