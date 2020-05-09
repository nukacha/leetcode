class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Dynamic Programming
        """
        # initialize
        table = [[i] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(table[0])):
            table[0][i] = i

        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                deletion = table[i - 1][j] + 1
                insertion = table[i][j - 1] + 1
                replacement = table[i - 1][j - 1]
                replacement += word1[i - 1] != word2[j - 1]
                table[i][j] = min(deletion, insertion, replacement)
        return table[-1][-1]
