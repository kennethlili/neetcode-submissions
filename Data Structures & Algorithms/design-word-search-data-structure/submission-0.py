class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.word
            char = word[i]
            if char == '.':
                for (key,val) in node.children.items():
                    if dfs(val, i+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i+1)
        return dfs(self.root, 0)
            
            

        
            
