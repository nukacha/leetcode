from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        sub_len = 0
        arr = []
        for num in nums:
            if num == 1:
                sub_len += 1
            else:
                arr.append(sub_len)
                sub_len = 0
        if sub_len == len(nums):
            return sub_len - 1
        arr.append(sub_len)
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        return max(arr[i] + arr[i - 1] for i in range(1, len(arr)))
