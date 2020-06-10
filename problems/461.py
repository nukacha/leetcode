class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        r = 0
        while xor != 0:
            if xor % 2 == 1:
                r += 1
            xor = xor // 2
        return r
