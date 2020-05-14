class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.is_end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            self.is_end = True
            return
        elif word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return self.is_end
        elif word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return True
        elif prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        else:
            return False
