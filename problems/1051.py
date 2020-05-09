from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(s != t for s, t in zip(heights, sorted(heights)))
