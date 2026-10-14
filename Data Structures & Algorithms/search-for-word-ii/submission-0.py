class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        ROW, COL = len(board), len(board[0])
        def insert(word):
            curr = root
            for char in word:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
            curr.word = word            
        for word in words:
            insert(word)
        res = []
        def dfs(node, r,c):
            outofbound = r<0 or c< 0 or r>= ROW or c>= COL
            if outofbound or board[r][c] == '*' or board[r][c] not in node.children: 
                return False
            currChar = board[r][c]
            board[r][c] = '*'
            child = node.children[currChar]
            if len(child.word) != 0:
                print(currChar)
                res.append(child.word)
                child.word = ""
            dfs(child, r+1,c)
            dfs(child, r-1,c)
            dfs(child, r,c+1)
            dfs(child, r,c-1)
            board[r][c] = currChar
        for r in range(ROW):
            for c in range(COL):
                dfs(root, r, c)
        return res


            
            


        
        