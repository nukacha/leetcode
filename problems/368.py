from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums.sort()
        set_dict = {num: {num} for num in nums}
        for num in nums:
            set_dict[num].update(
                max(
                    (set_dict[v] for v in set_dict if num % v == 0),
                    key=len
                )
            )
        return max(set_dict.values(), key=len)
