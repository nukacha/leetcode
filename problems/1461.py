class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2 ** k):
            if format(i, f'0{k}b') not in s:
                return False
        return True
