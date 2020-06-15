from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = {u: dict() for u, _, _ in times}
        for u, v, w in times:
            graph[u][v] = w
        time_dict = {K: 0}
        visited_set = {K}
        queue = [K]
        while queue:
            node = min(queue, key=time_dict.get)
            visited_set.add(node)
            if neib := graph.get(node):
                queue.extend(neib)
                queue = [v for v in queue if v not in visited_set]
            else:
                queue.remove(node)
                continue            
            now = time_dict[node]
            for k in neib:
                time_dict[k] = min(now + neib[k], time_dict.get(k, inf))
        if len(time_dict) != N:
            return -1
        else:
            return max(time_dict.values())
