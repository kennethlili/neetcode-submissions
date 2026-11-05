"""
Facts:
    move down/ right
    if go out of bound, path doesnt count
    we need to reach grid[m - 1][n - 1]
    count how many path to reach the goal
    m,n min len is 1, min path is 1
    starting from 0,0

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def nums_of_ways_to_reach(r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            isOutofBound = r >= m or c >= n
            if isOutofBound:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            down = nums_of_ways_to_reach(r + 1, c)
            right = nums_of_ways_to_reach(r, c + 1)
            memo[(r,c)] = down + right
            return memo[(r,c)]

        return nums_of_ways_to_reach(0, 0)
