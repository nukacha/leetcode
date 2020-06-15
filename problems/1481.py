from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        arr.sort(key=lambda v: (count[v], v))
        return len(set(arr[k:]))
