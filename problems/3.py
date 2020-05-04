class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        si = 0
        r = 0
        letter_dict = dict()
        for ti, letter in enumerate(s):
            if letter in letter_dict:
                si = max(si, letter_dict[letter] + 1)
            letter_dict[letter] = ti
            tmp_length = ti - si + 1
            r = max(r, tmp_length)
        return r
