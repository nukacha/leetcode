class Solution:
    def climbStairs(self, n: int) -> int:
        cnts = (1, 1)
        for _ in range(n - 1):
            cnts = cnts[1], sum(cnts)
        return cnts[1]  # Fibonacci number
