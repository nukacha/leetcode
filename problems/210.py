from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].add(u)
            indegree[u] += 1
        queue = deque(k for k, v in indegree.items() if v == 0)
        r = []
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            graph.pop(u)
            r.append(u)
        if len(r) == numCourses:
            return r
        else:
            return []
