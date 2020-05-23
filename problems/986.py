from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        r = []
        while i < len(A) and j < len(B):
            s = max(A[i][0], B[j][0])
            t = min(A[i][1], B[j][1])
            if s <= t:
                r.append([s, t])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return r
