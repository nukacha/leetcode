from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = max_right
            if max_right < tmp:
                max_right = tmp
        return arr
