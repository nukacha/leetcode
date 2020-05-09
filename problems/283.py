from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_cnt = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
            else:
                zero_cnt += 1
        for j in range(-1, -(zero_cnt + 1), -1):
            nums[j] = 0
