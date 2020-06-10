from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx_min = 0
        idx_max = len(nums) - 1
        while idx_min <= idx_max:
            idx = (idx_max + idx_min) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                idx_min = idx + 1
            else:
                idx_max = idx - 1
        return -1
