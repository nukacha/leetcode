from typing import List


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        roots = set(dict)
        replaced = list()
        for word in sentence.split():
            for i in range(1, len(word) + 1):
                if word[:i] in roots:
                    replaced.append(word[:i])
                    break
                if i == len(word):
                    replaced.append(word)
        return ' '.join(replaced)
