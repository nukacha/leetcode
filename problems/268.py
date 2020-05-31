from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in nums:
            if num < 0:
                num = ~num   
            if num < len(nums):
                nums[num] = ~nums[num]
        for i in range(len(nums)):
            if nums[i] > -1:
                return i
        return len(nums)
