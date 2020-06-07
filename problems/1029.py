from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        half_len = len(costs) // 2
        return sum(x[0] for x in costs[:half_len]) + sum(x[1] for x in costs[half_len:])
