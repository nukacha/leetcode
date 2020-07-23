from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        return min(nums[-i] - nums[4 - i] for i in range(1, 5))
