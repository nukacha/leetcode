from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zero_indices = [i for i, x in enumerate(arr) if x == 0]
        arr_end_index = len(arr) - 1
        for cnt, index in enumerate(zero_indices):
            insert_index = index + cnt
            if arr_end_index < insert_index:
                break
            arr.insert(insert_index, 0)
            arr.pop()
