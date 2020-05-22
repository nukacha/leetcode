class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        tmps = 0, 1
        for _ in range(1, N):
            tmps = tmps[1], sum(tmps)
        return tmps[1]
