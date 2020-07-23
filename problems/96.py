class Solution:
    memo = {0: 1, 1: 1}
    def numTrees(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = sum(
                self.numTrees(n - i - 1) * self.numTrees(i) for i in range(n)
            )
        return self.memo[n]
