from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        memo = {len(graph) - 1: [[len(graph) - 1]]}
        def dfs(i: int) -> List[List[int]]:
            if i in memo:
                return memo[i]
            paths = []
            for t in graph[i]:
                for path in dfs(t):
                    if path is not None:
                        paths.append([i, *path])
            memo[i] = paths
            return paths
        return dfs(0)
