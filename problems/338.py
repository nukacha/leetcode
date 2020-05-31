from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        r = [0] * (num + 1)
        for i in range(1, num + 1):
            r[i] = r[i // 2] + i % 2
        return r
