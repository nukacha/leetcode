from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[0])
        r = [None] * len(people)
        for h, k in people:
            i = cnt = 0
            while cnt < k or r[i] is not None:
                if r[i] is not None and r[i][0] < h:
                    i += 1
                else:
                    i += 1
                    cnt += 1
            r[i] = [h, k]
        return r
