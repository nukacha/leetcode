class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        l = 1
        while l <= r:
            m = (r + l) // 2
            q = num // m
            if q == m:
                if num % m:
                    return False
                else:
                    return True
            elif m < q:
                l = m + 1
            elif q < m:
                r = m - 1
        return False
