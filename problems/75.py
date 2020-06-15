from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]
        for n in nums:
            cnt[n] += 1
        cnt[1] += cnt[0]
        cnt[2] += cnt[1]
        for i in range(len(nums)):
            if i < cnt[0]:
                nums[i] = 0
            elif i < cnt[1]:
                nums[i] = 1
            else:
                nums[i] = 2
