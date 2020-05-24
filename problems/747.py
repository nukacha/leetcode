from math import inf
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        top1 = (-inf, -1)
        for i, n in enumerate(nums):
            if top1[0] < n:
                top2 = top1
                top1 = (n, i)
            elif top2[0] < n:
                top2 = (n, i)
        if top1[0] >= top2[0] * 2:
            return top1[1]
        else:
            return -1
