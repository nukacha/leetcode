from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        is_visited = [[False] * n for _ in range(m)]
        circles = []
        def search(x, y):
            flag = not (x in (0, m - 1) or y in (0, n - 1))
            circles.append((x, y))
            is_visited[x][y] = True
            coords = [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1)
            ]
            
            for nx, ny in coords:
                if not 0 <= nx < m:
                    continue
                elif not 0 <= ny < n:
                    continue
                elif is_visited[nx][ny]:
                    continue
                elif board[nx][ny] == 'X':
                    continue
                else:
                    flag &= search(nx, ny)
            return flag
                
        def fill(coords):
            for x, y in coords:
                board[x][y] = 'X'
                
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if is_visited[i][j]:
                    continue
                elif board[i][j] == 'O':
                    if search(i, j):
                        fill(circles)
                    circles = []
                else:
                    is_visited[i][j] = True
