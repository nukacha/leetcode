class Solution:
    memo = {i: i for i in range(4)}
    def numSquares(self, n: int) -> int:
        if n not in self.memo:         
            r = n
            for i in range(1, n):
                m = n - i ** 2
                if m < 0:
                    break
                r = min(r, self.numSquares(m) + 1)
            self.memo[n] = r
        return self.memo[n]
