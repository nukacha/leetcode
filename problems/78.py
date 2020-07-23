from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(2 ** len(nums)):
            choosed = reversed([b == '1' for b in format(i, 'b')])
            subset = [nums[j] for j, c in enumerate(choosed) if c]
            result.append(subset)
        return result
