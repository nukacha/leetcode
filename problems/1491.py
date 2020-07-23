from statistics import mean
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return mean(sorted(salary)[1:-1])
