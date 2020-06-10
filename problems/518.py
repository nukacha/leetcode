from collections import defaultdict
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(dict)
        def func(total, n):
            if total == 0:
                return 1
            if n <= 0 or total < 0:
                return 0
            if total in dp and n in dp[total]:
                return dp[total][n]
            r = func(total, n - 1)
            r += func(total - coins[n - 1], n)
            dp[total][n] = r
            return r
        return func(amount, len(coins))
