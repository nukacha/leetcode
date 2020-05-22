from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        sorted_char = sorted(s)
        sorted_char.sort(key=char_count.get, reverse=True)
        return ''.join(sorted_char)
