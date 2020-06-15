from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        intervals = []
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        arr.insert(0, 0)
        for i in range(len(arr) - 1):
            sidx = i
            eidx = len(arr) - 1
            while sidx <= eidx:
                idx = (sidx + eidx) // 2
                interval_sum = arr[idx] - arr[i]
                if interval_sum == target:
                    intervals.append((i, idx))
                    break
                elif interval_sum > target:
                    eidx = idx - 1
                else:
                    sidx = idx + 1
        intervals.sort(key=lambda x: x[1] - x[0])
        for i in range(len(intervals)):
            sidx1, eidx1 = intervals[i]
            len_i = eidx1 - sidx1
            for j in range(i + 1, len(intervals)):
                sidx2, eidx2 = intervals[j]
                if sidx1 <= sidx2 < eidx1:
                    continue
                elif sidx2 <= sidx1 < eidx2:
                    continue
                return len_i + eidx2 - sidx2
        return -1
