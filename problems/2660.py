class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1 = self.score(player1)
        s2 = self.score(player2)
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0

    def score(self, player: List[int]) -> int:
        c = 0
        s = 0
        for p in player:
            if c > 0:
                s += 2 * p
                c -= 1
            else:
                s += p

            if p == 10:
                c = 2
        return s
 
