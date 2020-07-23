class Solution:
    square_nums = {i * i for i in range(1, 317)}
    note = {}
    
    def winnerSquareGame(self, n: int) -> bool:
        if n < 1:
            return False
        if n in self.note:
            return self.note[n]
        if n in self.square_nums:
            return True
        else:
            for s in self.square_nums:
                if s < n and not self.winnerSquareGame(n - s):
                    self.note[n] = True
                    return True
            self.note[n] = False
            return False
