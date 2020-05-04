from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        h = (m + n + 1) // 2
        imin, imax = max(0, h - n), min(m, h)
        while True:
            i = (imin + imax) // 2
            j = h - i
            if i < m and 0 < j and nums1[i] < nums2[j - 1]:
                imin += 1
            elif 0 < i and j < n and nums2[j] < nums1[i - 1]:
                imax -= 1
            else:
                left_max = max(nums1[i - 1:i] + nums2[j - 1:j])
                if (m + n) % 2 == 1:
                    return left_max
                right_min = min(nums1[i:i + 1] + nums2[j:j + 1])
                return (left_max + right_min) / 2
