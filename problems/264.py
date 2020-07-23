class Solution:
    def nthUglyNumber(self, n: int) -> int:
        exp_2 = [2 ** i for i in range(32)]
        exp_3 = [3 ** i for i in range(20)]
        exp_5 = [5 ** i for i in range(14)]
        return sorted(exp_2[a] * exp_3[b] * exp_5[c] 
                      for a in range(32) 
                      for b in range(20) 
                      for c in range(14))[n - 1]
