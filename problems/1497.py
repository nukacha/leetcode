from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr[:] = [n % k for n in arr]
        counter = Counter(arr)
        for i in range(k // 2):
            j = (k - i) % k
            if j == i and counter[i] % 2 != 0:
                return False
            if counter[i] != counter[j]:
                return False
        return True
