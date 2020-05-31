from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = max(
            horizontalCuts[0] - 0,
            h - horizontalCuts[-1]
        )
        if len(horizontalCuts) != 1:
            max_h = max(
                max_h,
                max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts)))
            )
        max_w = max(
            verticalCuts[0] - 0,
            w - verticalCuts[-1]
        )
        if len(verticalCuts) != 1:
            max_w = max(
                max_w,
                max(verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts)))
            )
        return (max_h * max_w) % 1000000007
