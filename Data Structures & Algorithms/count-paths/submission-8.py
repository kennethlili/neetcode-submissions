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
        prev = [1] * (n + 1)
        for r in range(m - 2, -1, -1):
            curr = prev
            for c in range(n - 2, -1, -1):
                curr[c] = prev[c] + curr[c + 1]
            prev = curr

        return prev[0]
