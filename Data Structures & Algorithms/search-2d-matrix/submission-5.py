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
        top,bot = 0,len(matrix) -1
        row = len(matrix) -1
        while top <= bot:
            mid = (top + bot)//2
            num = matrix[mid][-1]
            if target > num:
                # go bot
                top = mid +  1


            elif target < num:
                bot = mid -1
                row = min(row, mid)
            else:
                return True
        left,right = 0 , len(matrix[0]) -1
        while left <= right:
            mid = (left + right)//2
            num = matrix[row][mid]
            if target > num:
                # go right
                left = mid +  1
            elif target < num:
                right = mid -1
            else:
                return True
        return False
