from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = [None] * len(s)
        for i, j in enumerate(indices):
            r[j] = s[i]
        return ''.join(r)
