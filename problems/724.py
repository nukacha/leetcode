from typing import List

import numpy as np


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cumsum_f = np.cumsum(nums)
        cumsum_r = np.cumsum(nums[::-1])[::-1]
        for i, v in enumerate(cumsum_f - cumsum_r):
            if v == 0:
                return i
        return -1
