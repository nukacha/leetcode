class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i == len(s):
                return True
            elif c == s[i]:
                i += 1
        if i < len(s):
            return False
        else:
            return True
