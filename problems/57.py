from bisect import bisect
from itertools import chain
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flags = [self.is_overlapping(itv, newInterval) for itv in intervals]
        if not any(flags):
            self.insort(intervals, newInterval)
            return intervals
        overlapping = [itv for itv, flag in zip(intervals, flags) if flag]
        nums = [n for n in chain(*overlapping, newInterval)]
        merged = [min(nums), max(nums)]
        r = [itv for itv, flag in zip(intervals, flags) if not flag]
        self.insort(r, merged)
        return r
        
    def insort(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect([itv[0] for itv in intervals], newInterval[0])
        intervals.insert(idx, newInterval)
        
    def is_overlapping(self, interval1: List[int], interval2: List[int]) -> bool:
        r = False
        r |= interval2[0] <= interval1[0] <= interval2[1]
        r |= interval2[0] <= interval1[1] <= interval2[1]
        r |= interval1[0] <= interval2[0] <= interval1[1]
        r |= interval1[0] <= interval2[0] <= interval1[1]
        return r
