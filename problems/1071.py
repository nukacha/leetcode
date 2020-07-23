def dividable(str1: str, str2: str) -> bool:
    return str2 in str1 and str1.replace(str2, '') == ''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            short, long = str2, str1
        else:
            short, long = str1, str2
        for i in range(1, len(short) + 1):
            if len(short) % i != 0:
                continue
            x = short[:len(short) // i]
            if dividable(str1, x) and dividable(str2, x):
                return x
        return ''
