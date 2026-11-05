"""
Facts:
    move down/ right
    if go out of bound, path doesnt count
    we need to reach grid[m - 1][n - 1]
    count how many path to reach the goal
    m,n min len is 1, min path is 1
    starting from 0,0
Bound:
    r: [0, m ]
    c: [0, n]
order:
    r: big - small
    c: big - small
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m-1][n-1] == 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp[r][c] = 1
                    continue
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
