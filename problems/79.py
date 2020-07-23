from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def search(pos, i, j):
            if not (-1 < i < m and -1 < j < n):
                return False
            elif pos == len(word):
                return False
            elif (c := board[i][j]) != word[pos]:
                return False
            elif pos == len(word) - 1:
                return True
            board[i][j] = '#'
            coords = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))
            found = any(search(pos + 1, x, y) for x, y in coords)
            board[i][j] = c
            return found
        return any(search(0, x, y) for x in range(m) for y in range(n))
