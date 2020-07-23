from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = {i: set() for i in range(1, n + 1)}
        indegree = {i: 0 for i in range(1, n + 1)}
        for u, v in dependencies:
            graph[u].add(v)
            indegree[v] += 1
        r = 0
        while roots := [i for i in range(1, n + 1) if i in graph and indegree[i] == 0]:
            roots = sorted(roots, key=lambda x: len(graph[x]), reverse=True)[:k]
            for root in roots:
                for child in graph[root]:
                    indegree[child] -= 1
                graph.pop(root)
            r += 1
        return r
