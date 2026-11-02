"""
questions:
are we guratee to have island?

actions:
take: if grid == '1'
skip: if grid == '0'

visited, to avoid revisiting the same node

for each grid item in grid, dfs
if dfs 
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW , COL = len(grid) , len(grid[0])
        def dfs(r,c):
            outofbound = r < 0 or r >= (ROW) or c < 0 or c >= COL
            if outofbound or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r + 1,c)
            dfs(r -1 ,c)
            dfs(r,c+ 1)
            dfs(r,c-1 )

        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        return res
            