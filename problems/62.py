from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1; n -=1
        return factorial(m + n) // (factorial(m) * factorial(n))
