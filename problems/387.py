class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx_dict = {c: i for i, c in enumerate(s)}
        appeared_set = set()
        for c in s:
            if c in appeared_set and c in idx_dict:
                idx_dict.pop(c)
            else:
                appeared_set.add(c)
        if len(idx_dict):
            return sorted(idx_dict.values())[0]
        else:
            return -1
