from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            arr[i] = arr[i] % 2 == 1
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i - 1] == 1
        arr.insert(0, 0)
        sum_odd = sum(arr)
        r = 0
        for i in range(len(arr)):
            if arr[i]:
                r += len(arr) - i - sum_odd
                sum_odd -= 1
            else:
                r += sum_odd
        return r % 1000000007
