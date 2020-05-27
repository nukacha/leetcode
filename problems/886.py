from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        set1 = set([dislikes[-1][0]])
        set2 = set([dislikes[-1][1]])
        dislikes.pop()
        isolation = None
        while any(v is not None for v in dislikes):
            for i, dislike in enumerate(dislikes):
                if dislike is None:
                    continue
                elif dislike[0] in set1:
                    if dislike[1] in set1:
                        return False
                    set2.add(dislike[1])
                elif dislike[0] in set2:
                    if dislike[1] in set2:
                        return False
                    set1.add(dislike[1])
                elif dislike[1] in set1:
                    set2.add(dislike[0])
                elif dislike[1] in set2: 
                    set1.add(dislike[0])
                elif isolation == i:
                    set1.add(dislike[0])
                    set2.add(dislike[1])
                elif isolation is None:
                    isolation = i
                    continue
                isolation = None
                dislikes[i] = None
        return True
