from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx_min = 0
        idx_max = len(nums)
        while idx_min != idx_max:
            idx = (idx_max + idx_min) // 2
            if nums[idx] < target:
                idx_min = idx + 1
            else:
                idx_max = idx
        return idx_min
