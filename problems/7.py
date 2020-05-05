class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        digits = []
        while x:
            digits.append(x % 10)
            if len(digits) > 10:
                break
            x //= 10
        r = sign * sum(v * (10 ** i) for i, v in enumerate(digits[::-1]))
        r = 0 if r > 2 ** 31 - 1 else r
        r = 0 if r < -2 ** 31 else r
        return r
