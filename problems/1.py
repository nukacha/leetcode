from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, v in enumerate(nums):
            another = target - v
            if another in num_dict:
                return [i, num_dict[another]]
            num_dict[v] = i
