"""
search for word inside words in the grid
grid
    move in 4 directions-> horizon, vertical
    we cannot mise the same cell more than once in a word

for each word, do a dfs on the word

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Solution:
    def initTries(self, words):
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
        return root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.initTries(words)

        ROW, COL = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []

        def dfs(r, c, visited, curr):
            if r >= ROW or r < 0 or c >= COL or c < 0 or (r, c) in visited:
                return False

            ch = board[r][c]
            if ch not in curr.children:
                return False

            if curr.children[ch].word:
                res.append(curr.children[ch].word)
                curr.children[ch].word = ""

            visited.add((r, c))

            for tr, tc in DIRS:
                if dfs(r + tr, c + tc, visited, curr.children[ch]):
                    return True
            visited.remove((r, c))
            return False

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, set(), root)

        return res
