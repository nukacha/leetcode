from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        tmp1 = tmp2 = 0
        for i in range(2, len(cost) + 1):
            tmp1, tmp2 = tmp2, min(tmp1 + cost[i - 2], tmp2 + cost[i - 1])
        return tmp2
