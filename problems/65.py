import re


class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r'^[-+]?(\d+\.|\.\d+|\d+(\.\d+)?)(e[-+]?\d+)?$')
        return re.match(pattern, s.strip()) is not None
