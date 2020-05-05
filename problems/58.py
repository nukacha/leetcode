class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w_list = s.strip().split()
        return len(w_list[-1]) if w_list else 0
