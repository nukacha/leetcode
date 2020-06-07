from random import randint
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        w = sorted(enumerate(w))
        for i in range(1, len(w)):
            w[i] = w[i][0], w[i][1] + w[i - 1][1]
        self.w = w
            
    def search(self, n: int) -> int:
        idx_min = 0
        idx_max = len(self.w) - 1
        while idx_min != idx_max:
            idx = (idx_max + idx_min) // 2
            if self.w[idx][1] < n:
                idx_min = idx + 1
            else:
                idx_max = idx
        return self.w[idx_min][0]

    def pickIndex(self) -> int:
        n = randint(1, self.w[-1][1])
        return self.search(n)
