class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(c for c in s if c.isalnum()).lower()
        i, j = 0, len(filtered) - 1
        while i < j:
            if filtered[i] != filtered[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
