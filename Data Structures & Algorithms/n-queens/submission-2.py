"""
only place n queens on a n x n chessboard
the queen must be place horizontally, vertically, and diagonally.

how do we know we placed n Q?

"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        main_dia = set()
        anti_dia = set()
        res = []

        def buildCleanBoard():
            board = []
            for _ in range(n):
                board.append(["."] * n)
            return board

        def backtrack(r, curr):
            if len(curr) == n:
                board = buildCleanBoard()
                for qr, qc in curr:
                    board[qr][qc] = "Q"
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r - c) in main_dia or (r + c) in anti_dia:
                    continue
                curr.append((r, c))
                cols.add(c)
                main_dia.add(r - c)
                anti_dia.add(r + c)
                backtrack(r + 1, curr)
                curr.pop()
                cols.remove(c)
                main_dia.remove(r - c)
                anti_dia.remove(r + c)

        backtrack(0, [])
        return res
