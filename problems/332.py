from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for airports in graph.values():
            airports.sort(reverse=True)
        itinerary = []
        stack = ['JFK']
        while stack:
            if airports := graph[stack[-1]]:
                stack.append(airports.pop())
            else:   # a dead end
                itinerary.append(stack.pop())
        return reversed(itinerary)
