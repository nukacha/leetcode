from collections import defaultdict
from itertools import chain
from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)
        flag = {k: True for k in graph}
        def func(cource):
            if flag.get(cource):
                for v in graph[cource].copy():
                    graph[cource].update(func(v))
                flag[cource] = False
            return graph.get(cource, ())
        for k in flag:
            func(k)
        return [u in graph[v] for u, v in queries]
