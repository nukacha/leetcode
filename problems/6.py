class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        lines = [str() for i in range(numRows)]
        for i, c in enumerate(s):
            j = i % (2 * (numRows - 1))
            if j < numRows:
                lines[j] += c
            else:
                lines[2 * (numRows - 1) - j] += c
        return ''.join(lines)
