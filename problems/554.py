from collections import Counter
from typing import List

import numpy as np


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cumsum_cnt = Counter()
        [cumsum_cnt.update(np.cumsum(r[:-1])) for r in wall]
        if len(cumsum_cnt) == 0:
            return len(wall)
        return len(wall) - cumsum_cnt.most_common(1)[0][1]
