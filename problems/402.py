from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = deque()
        for digit in num:
            while result and k and digit < result[-1]:
                result.pop()
                k -= 1
            result.append(digit)
        for _ in range(k):
            result.pop()
        return ''.join(result).lstrip('0') or '0'
