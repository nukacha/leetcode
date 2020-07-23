from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr2) != 0:
            int_to_idx = {v: i for i, v in enumerate(arr2)}
            max_arr2 = max(arr2)
            arr1.sort(key=lambda x: int_to_idx.get(x, x + max_arr2))
        else:
            arr1.sort()
        return arr1
