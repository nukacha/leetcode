from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if sum(n == 0 for n in arr) > 1:
            return True
        num_set = set(arr)
        num_set -= set([0])
        return len(num_set) * 2 != len(num_set | set(n * 2 for n in num_set))