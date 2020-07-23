from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff_set = set(arr[i] - arr[i - 1] for i in range(1, len(arr)))
        return len(diff_set) == 1
