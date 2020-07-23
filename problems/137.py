from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return min(cnt, key=cnt.get)
