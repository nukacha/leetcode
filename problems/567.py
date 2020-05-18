from collections import Counter, deque


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)
        s2_queue = deque()
        for c in s2[:len(s1) - 1]:
            s2_queue.appendleft(c)
        for c in s2[len(s1) - 1:]:
            s2_queue.appendleft(c)
            if Counter(s2_queue) == s1_cnt:
                return True
            s2_queue.pop()
        return False
