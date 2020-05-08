class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        r = 1
        if n % 3 == 1:
            r *= 4
            n -= 4
        elif n % 3 == 2:
            r *= 2
            n -= 2    
        r *= 3 ** (n // 3)
        return r
