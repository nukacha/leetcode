from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev_row = self.getRow(rowIndex - 1)
            row = [sum(prev_row[i: i + 2]) for i in range(rowIndex - 1)]
            return [1] + row + [1]
