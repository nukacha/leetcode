class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        digits = []
        while True:
            columnNumber -= 1
            digits.append(columnNumber % 26)
            columnNumber //= 26
            if columnNumber == 0:
                break
        digits.reverse()
        return "".join(chr(65 + x) for x in digits)
