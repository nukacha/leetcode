from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        accum_dict = {0: -1}
        v = r = 0
        for i, num in enumerate(nums):
            v += 1 if num else -1
            if (j := accum_dict.get(v)) is not None:
                r = max(r, i - j)
            else:
                accum_dict[v] = i
        return r
