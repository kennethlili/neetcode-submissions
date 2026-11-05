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
        dp_r1 = [0] * (n + 1)


        for r in range(m - 1, -1, -1):
            dp_r = dp_r1
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp_r[c] = 1
                    continue
                dp_r[c] = dp_r1[c] + dp_r[c + 1]
                dp_r1 = dp_r

        return dp_r1[0]
