class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bit_len = len(bin(N)) - 2
        return N ^ (2 ** bit_len -1)
