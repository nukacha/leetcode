class Solution:
    def findComplement(self, num: int) -> int:
        bit_len = len(bin(num)) - 2
        return num ^ (2 ** bit_len -1)
