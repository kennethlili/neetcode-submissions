"""
Facts:
    the board is valid
        - row 1-9 without duplicates
        - col 1-9 without duplicates
        - grid 1-9 without duplicates
    return true if valid, false otherwise
        -doesnt need to be full or be solvable
    the digit is a string
    "." stands for empty

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_lookup = [set() for i in range(9)]
        col_lookup = [set() for i in range(9)]
        grid_lookup = [set() for i in range(9)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue
                grid_id = r // 3 * 3 + c // 3
                row, col, grid = row_lookup[r], col_lookup[c], grid_lookup[grid_id]
                if val in row or val in col or val in grid:
                    return False
                row.add(val)
                col.add(val)
                grid.add(val)
        return True
