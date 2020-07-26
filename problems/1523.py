class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2:
            return (high - low) // 2 + 1
        else:
            return (high - low + 1) // 2
