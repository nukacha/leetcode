from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        interval_dict = {}
        bouquet = 0
        for i, day in sorted(enumerate(bloomDay), key=lambda x: (x[1], x[0])):
            if i + 1 in interval_dict and i - 1 in interval_dict:
                sidx = interval_dict.pop(i - 1)
                eidx = interval_dict.pop(i + 1)
                interval_dict[sidx] = eidx
                interval_dict[eidx] = sidx
                left_bouquet = (abs(i - 1 - sidx) + 1) // k
                right_bouquet = (abs(i + 1 - eidx) + 1) // k
                bouquet += (abs(sidx - eidx) + 1) // k - left_bouquet - right_bouquet
            elif i + 1 in interval_dict:
                eidx = interval_dict.pop(i + 1)
                interval_dict[i] = eidx
                interval_dict[eidx] = i
                if (abs(eidx - i) + 1) % k == 0:
                    bouquet += 1
            elif i - 1 in interval_dict:
                sidx = interval_dict.pop(i - 1)
                interval_dict[i] = sidx
                interval_dict[sidx] = i
                if (abs(sidx - i) + 1) % k == 0:
                    bouquet += 1
            else:
                interval_dict[i] = i
                if k == 1:
                    bouquet += 1
            if bouquet >= m:
                return day
        return -1
