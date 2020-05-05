from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [x >> 1 ^ x for x in range(2 ** n)]