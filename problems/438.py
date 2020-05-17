from collections import Counter, deque
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        s_queue = deque()
        for c in s[:len(p) - 1]:
            s_queue.appendleft(c)
        r = []
        for i, c in enumerate(s[len(p) - 1:]):
            s_queue.appendleft(c)
            if Counter(s_queue) == p_cnt:
                r.append(i)
            s_queue.pop()
        return r
