from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        tail = nums[-k:]
        for i in range(len(nums) - 1, -1, -1):
            nums[i] = nums[i - k]
        nums[:k] = tail
