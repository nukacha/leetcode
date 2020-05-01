# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [a ** 2 for a in A]
        A.sort()
        return A
