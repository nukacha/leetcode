from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.maxWidth = maxWidth
        word_lens = [len(w) for w in words]
        result = []
        i, j = 0, 1
        while j < len(words):
            line_words = words[i:j]
            next_len = sum(word_lens[i:j + 1]) + j - i
            if next_len > maxWidth:
                result.append(self.justify(line_words))
                i = j
                j += 1
            else:
                j += 1
        result.append(self.leftJustify(words[i:j]))
        return result
    
    def justify(self, words: List[str]) -> str:
        sum_word_lens = sum(len(w) for w in words)
        spaces_len = self.maxWidth - sum_word_lens
        spaces_num = len(words) - 1
        if len(words) == 1:
            return words[0] + ' ' * spaces_len
        for i in range(spaces_num):
            words.insert(
                i * 2 + 1,
                ' ' * (
                    spaces_len // spaces_num
                    + (i < spaces_len % spaces_num)
                )
            )
        return ''.join(words)
        
    def leftJustify(self, words: List[str]) -> str:
        line = ' '.join(words)
        line += ' ' * (self.maxWidth - len(line))
        return line
