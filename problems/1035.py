from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        nums = set(A) & set(B)
        A = [i for i in A if i in nums]
        B = [i for i in B if i in nums]
        del nums
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):  
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
