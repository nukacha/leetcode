import re


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        match = re.match(r'^[-+]?\d+', str)
        if match is None:
            return 0
        r = int(match.group())
        r = min(r, 2 ** 31 - 1)
        r = max(r, -2 ** 31)
        return r
