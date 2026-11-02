"""
Actions:
1. insert
iterative the string
add the TrieNode for each char
at the end we mark the word flag to be true
O(n)
return?

2. search
word -> iterative
return True if self.word

3. startsWith
word -> iterative
return False if children[ch] not found
"""

class TrieNode:
    def __init__(self):
        self.children ={}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
        