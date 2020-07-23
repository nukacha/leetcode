from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums.insert(0, 0)
        sum_array = sorted(nums[j] - nums[i] for i in range(n) for j in range(i + 1, n + 1))
        return sum(sum_array[left - 1: right]) % 1000000007
