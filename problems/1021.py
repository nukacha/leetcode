class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        S = list(S)
        i = 0
        cnt = 1
        for j in range(1, len(S)):
            if S[j] == '(':
                if cnt == 0:
                    i = j
                cnt += 1
            else:
                if cnt == 1:
                    S[i] = S[j] = ''
                cnt -= 1
        return ''.join(c for c in S if c != '')
