from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_idx = 0; max_idx = len(nums) - 1
        while min_idx < max_idx:
            mid_idx = (min_idx + max_idx) // 2
            mid = nums[mid_idx]
            if nums[min_idx] == mid == nums[max_idx]:
                min_idx += 1
                max_idx -= 1
            elif nums[max_idx] >= mid:
                max_idx = mid_idx
            else:
                min_idx = mid_idx + 1
        return nums[min_idx]
