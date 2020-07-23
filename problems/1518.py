class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        r = empty = 0
        while numBottles != 0:
            empty += numBottles
            r += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        return r
