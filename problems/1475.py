from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        r = []
        for i in range(len(prices)):
            l = [v for v in prices[i + 1:] if v <= prices[i]]
            r.append(prices[i] - l[0] if l else prices[i])
        return r
