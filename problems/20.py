class Solution:
    def isValid(self, s: str) -> bool:
        opened = list()
        brackets_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in brackets_dict:
                opened.append(c)
                continue
            elif not opened:
                return False
            last_opened = opened.pop()
            if c != brackets_dict[last_opened]:
                return False
        return False if opened else True
