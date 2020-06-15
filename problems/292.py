class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 1:
            return False
        return n % 4 != 0
