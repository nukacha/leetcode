from math import inf
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [inf] * (len(dungeon[0]) - 1) + [1]
        for row in dungeon[::-1]:
            for j in range(len(dungeon[0]) - 1, -1, -1):
                dp[j] = max(min(dp[j:j + 2]) - row[j], 1)
        return dp[0]
