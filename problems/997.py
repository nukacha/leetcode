from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        n_trusted = [0] * N
        has_trust = [False] * N
        for a, b in trust:
            n_trusted[b - 1] += 1
            has_trust[a - 1] = True
        judge_list = [i for i in range(N) if n_trusted[i] == N - 1 and not has_trust[i]]
        if len(judge_list) == 1:
            return judge_list[0] + 1
        else:
            return -1
