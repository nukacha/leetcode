from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0; n = len(citations)
        min_idx = 0; max_idx = n - 1
        while min_idx <= max_idx:
            idx = (min_idx + max_idx) // 2
            if citations[idx] >= (nh := n - idx):
                max_idx = idx - 1
                h = nh
            else:
                min_idx = idx + 1
        return h
