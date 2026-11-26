"""
board, word
    may have the lower or upper case eng char
return True if word is exist in board
path
    4 dirs left, right, low, upper
    reuse the cell that used


"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def helper(i, r, c):
            if i >= len(word):
                return True
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in visited:
                return False
            visited.add((r, c))
            ch = board[r][c]
            if ch == word[i]:
                for nr, nc in DIRS:
                    if helper(i + 1, r + nr, c + nc):
                        return True
            visited.remove((r, c))
            return False

        for r in range(ROW):
            for c in range(COL):
                if helper(0, r, c):
                    return True
        return False
