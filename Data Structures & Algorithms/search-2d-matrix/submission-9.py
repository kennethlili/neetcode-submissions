"""
facts:
    m x n matrix, integer 2-d arr
        sorted horizonally and overall
    return true if target exist in martrix, false otherwise
    runs in O(log(m * n)) time

    how do we perform a bin search on a 2d grid
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        
        while  top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                # go bot
                top = row + 1

            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # print(row)
                left, right = 0, len(matrix[row]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    num = matrix[row][mid]
                    if target > num:
                        # go right
                        left = mid + 1
                    elif target < num:
                        right = mid - 1
                    else:
                        return True
                return False
        if top > bot:
            return False
        # row = (top + bot)// 2
        
        return False
