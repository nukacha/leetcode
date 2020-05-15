from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        all_sum = sum(A)
        sums = [
            self.maxSubarraySum(A),
            all_sum + self.maxSubarraySum([-a for a in A[1:]]),
            all_sum + self.maxSubarraySum([-a for a in A[:-1]])
        ]
        return max(sums)
    
    def maxSubarraySum(self, A: List[int]) -> int:
        current_sum = 0
        max_sum = A[0]
        for a in A  :
            current_sum += a
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
