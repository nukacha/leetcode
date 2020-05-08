from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        if A[0] >= A[1] or A[-2] <= A[-1]:
            return False
        is_increasing = True
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                return False
            elif A[i] < A[i + 1] and not is_increasing:
                return False
            elif A[i] > A[i + 1] and is_increasing:
                is_increasing = False
        return True
