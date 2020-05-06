from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_int = len(nums)
        for i in range(max_int):
            j = nums[i] - 1
            while -1 < j < max_int:
                tmp = nums[j]
                if j + 1 == tmp:
                    break
                nums[j] = j + 1
                j = tmp - 1
        for i, num in enumerate(nums, 1):
            if i != num:
                return i
        return max_int + 1
