from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [[-1] * n for i in range(m)]
        d[0][0] = grid[0][0]
        coords = [(0, 0)]
        while d[m - 1][n - 1] == -1:
            x, y = coords.pop(0)
            if x < m - 1 and d[x + 1][y] == -1:
                dd = d[x][y] + grid[x + 1][y]
                d[x + 1][y] = dd
                coords.append((x + 1, y))
            if y < n - 1 and d[x][y + 1] == -1:
                dr = d[x][y] + grid[x][y + 1]
                d[x][y + 1] = dr
                coords.append((x, y + 1))
            coords.sort(key=lambda c: d[c[0]][c[1]])
        return d[m - 1][n - 1]
