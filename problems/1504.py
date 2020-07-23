from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(1, n):  
                if mat[i][j] == 0:
                    continue
                mat[i][j] += mat[i][j - 1]

        ans = 0
        for j in range(n):  
            stack = list()
            n_sub = 0
            for i in range(m - 1, -1, -1):  
                cur_h = 1
                cur_w = mat[i][j]
                while stack and cur_w < stack[-1][0]:
                    pre_w, pre_h = stack.pop()
                    n_sub -= pre_h * (pre_w - cur_w)
                    cur_h += pre_h
                n_sub += cur_w 
                ans += n_sub
                stack.append((cur_w, cur_h))
        return ans
