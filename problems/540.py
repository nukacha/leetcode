from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        min_i = 1
        max_i = len(nums) - 2
        i = len(nums) // 2
        while not self.isSingle(i, nums):
            if ((i % 2 and nums[i] == nums[i + 1])
                or
                (i % 2 == 0 and nums[i] == nums[i - 1])):
                max_i = i
            else:
                min_i = i
            i = (min_i + max_i) // 2
        return nums[i]
        
    def isSingle(self, i, nums):
        return nums[i - 1] != nums[i] != nums[i + 1]
