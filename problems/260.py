from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_xor = reduce(xor, nums)    # ans1 ^ ans2
        single_one = (nums_xor - 1) & nums_xor ^ nums_xor
        ans1 = 0
        for num in nums:
            if (single_one & num) != 0:
                ans1 ^= num     # (single_one & ans2) == 0
        ans2 = ans1 ^ nums_xor
        return [ans1, ans2]
