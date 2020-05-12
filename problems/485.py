from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        bins = ''.join(str(i) for i in nums)
        return max(len(con) for con in bins.split('0'))
