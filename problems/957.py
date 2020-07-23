from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        row = int(''.join(map(str, cells)), 2)
        i = 0
        seen = dict()
        while i < N:
            row = ~((row << 1) ^ (row >> 1)) & 126
            if row not in seen:
                seen[row] = i
                i += 1
            else:
                i = N - ((N - 1 - i) % (i - seen[row]))
        return list(format(row, '08b'))
