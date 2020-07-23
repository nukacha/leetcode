class Solution:
    """
    Rabin-Karp string search algorithm with rolling hash
    """

    base = 1007
    mod = 10 ** 9 + 7

    def longestDupSubstring(self, S: str) -> str:
        self.init_hash(S)
        min_len = 0; max_len = len(S) - 1
        while min_len < max_len:
            mid_len = (min_len + max_len + 1) // 2
            subst = self.dupSubstring(S, mid_len)
            if subst != '':
                min_len = mid_len
            else:
                max_len = mid_len - 1
        return self.dupSubstring(S, min_len)
    
    def init_hash(self, S):
        hash_l = [0] * (len(S) + 1)
        power_l = [1] * (len(S) + 1)
        for i, c in enumerate(S):
            hash_l[i + 1] = (hash_l[i] * self.base + ord(c)) % self.mod
            power_l[i + 1] = (power_l[i] * self.base) % self.mod
        self.hash_l = hash_l
        self.power_l = power_l
        
    def calc_hash(self, i, j):
        h = self.hash_l[j] - self.hash_l[i] * self.power_l[j - i]
        return h % self.mod
            
    def dupSubstring(self, S: str, n: int) -> str:
        hash_set = set()
        for i in range(len(S) - n + 1):
            if (h := self.calc_hash(i, i + n)) not in hash_set:
                hash_set.add(h)
            elif (subst := S[i:i + n]) in S[:i + n - 1]:
                return subst
        return ''
