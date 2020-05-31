from heapq import nlargest
from operator import mul
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return mul(*(i - 1 for i in nlargest(2, nums)))
