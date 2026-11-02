"""
Design a data structure that supports adding new words and searching for existing words.
WordDictionary Class:
    void addWord(word) Adds word to the data structure.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Constraint:
word small
lowercase only
at most 2 '.' for search
10000 calls

Trie
addWord

search:
    iterate the word char
     if char == '.'
        go thru every child

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False  # Flag to determine whether the end of the word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if i == len(word):
                return curr.word
            char = word[i]
            res = False

            if char == ".":
                for ch, node in curr.children.items():
                    res = res or dfs(node, i + 1)
            else:
                if char not in curr.children:
                    res = False
                else:
                    res = res or dfs(curr.children[char], i + 1)

            return res

        return dfs(self.root, 0)
