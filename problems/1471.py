from typing import List


class Solution:
    def median(self, arr: List[int]) -> int:
        return arr[(len(arr) - 1) // 2]

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        med = self.median(arr)
        arr.sort(reverse=True, key=lambda x: (abs(x - med), x))
        return arr[:k]
