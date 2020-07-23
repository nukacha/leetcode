from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {i: set() for i in range(n)}
        r = [1] * n
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        counter = {}
        
        def dfs(node):
            children = graph.pop(node)
            label = labels[node]
            cnt = {label: 1}
            for child in children:
                if child in graph:
                    dfs(child)
                    for k, v in counter[child].items():
                        if k in cnt:
                            cnt[k] += v
                        else:
                            cnt[k] = v
                r[node] = cnt[label]
            counter[node] = cnt
        dfs(0)
        return r
