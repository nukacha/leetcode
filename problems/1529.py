class Solution:
    def minFlips(self, target: str) -> int:
        r = 0
        mode = '0'
        for t in target:
            if t != mode:
                r += 1
            mode = t
        return r