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

        def backtrack(r, curr):
            if len(curr) == n:
                board = [["."] * n for _ in range(n)]
                for qr, qc in curr:
                    board[qr][qc] = "Q"
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                main,anti = r-c, r+c
                if c in cols or main in main_dia or anti in anti_dia:
                    continue
                curr.append((r, c))
                cols.add(c)
                main_dia.add(main)
                anti_dia.add(anti)
                backtrack(r + 1, curr)
                curr.pop()
                cols.remove(c)
                main_dia.remove(main)
                anti_dia.remove(anti)

        backtrack(0, [])
        return res
