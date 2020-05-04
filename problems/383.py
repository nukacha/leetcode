from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_cnt = Counter(magazine)
        for letter in ransomNote:
            if letter_cnt[letter] <= 0:
                return False
            letter_cnt[letter] -= 1
        return True
