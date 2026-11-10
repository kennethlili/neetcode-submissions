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
                if val in row_lookup[r] or val in col_lookup[c] or val in grid_lookup[grid_id]:
                    return False
                row_lookup[r].add(val)
                col_lookup[c].add(val)
                grid_lookup[grid_id].add(val)
        return True
