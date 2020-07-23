class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        for i in range(start + 2, start + 2 * n, 2):
            start ^= i
        return start
