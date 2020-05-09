from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -float('inf')
        top3 = set(nums[:3])
        for n in nums:
            if n in top3:
                continue
            elif len(top3) < 3:
                top3.add(n)
            elif min(top3) < n:
                top3.add(n)
                top3.remove(min(top3))
        return min(top3) if len(top3) == 3 else max(top3)
