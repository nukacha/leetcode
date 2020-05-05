from typing import List
from itertools import chain


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid = True
        for i in range(9):
            is_valid &= self.isValidBoxes(board[i])
            is_valid &= self.isValidBoxes([x[i] for x in board])
            j, k = i // 3, i % 3
            is_valid &= self.isValidBoxes(
                [x[3 * j: 3 * (j + 1)] for x in board[3 * k: 3 * (k + 1)]]
            )
            if not is_valid:
                return False
        return True
        
    def isValidBoxes(self, boxes: List) -> bool:
        if len(boxes) == 3:
            boxes = list(chain(*boxes))
        boxes = [x for x in boxes if x != '.']
        return len(boxes) == len(set(boxes))
