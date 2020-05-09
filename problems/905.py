from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenA = [n for n in A if n % 2 == 0]
        oddA = [n for n in A if n % 2 == 1]
        return evenA + oddA
