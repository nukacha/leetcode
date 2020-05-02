# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return sum(stone in jewels for stone in S)
