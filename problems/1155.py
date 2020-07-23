class Solution:
    def __init__(self):
        self.memo = [[None] * 1001 for _ in range(31)]
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < 1:
            return 0
        elif self.memo[d][target] is not None:
            return self.memo[d][target]
        elif d == 1:
            self.memo[d][target] = int(target <= f)
            return self.memo[d][target]
        self.memo[d][target] = 0
        for i in range(1, f + 1):
            r = self.numRollsToTarget(d - 1, f, target - i) 
            self.memo[d][target] += r
        return self.memo[d][target] % 1000000007
