from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0
        l_cnt = Counter(s[:1])
        r_cnt = Counter(s[1:])
        r = len(l_cnt) == len(r_cnt)
        for i in range(1, len(s) - 1):
            l_cnt[s[i]] += 1
            r_cnt[s[i]] -= 1
            if r_cnt[s[i]] == 0:
                r_cnt.pop(s[i])
            r += len(l_cnt) == len(r_cnt)
        return int(r)
