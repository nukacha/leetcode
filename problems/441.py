class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(n + 1):
            n -= i
            if n <= 0:
                return i - (n < 0)
