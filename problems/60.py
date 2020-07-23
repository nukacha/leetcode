from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        permutation = []
        k -= 1
        while len(nums) != 0:
            n -= 1
            idx, k = divmod(k, factorial(n))
            permutation.append(nums.pop(idx))
        return ''.join(map(str, permutation))
