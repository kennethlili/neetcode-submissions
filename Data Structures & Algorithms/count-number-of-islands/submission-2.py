class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c] == "1"  and (r,c) not in visited):
                    self.dfs(grid, r,c,visited)
                    res += 1
        return res
        
    def dfs(self,grid,r,c,visited):
        ROW, COL = len(grid), len(grid[0])
        isoutofbound = r > ROW -1 or c > COL -1 or r< 0 or c < 0
        if(isoutofbound or (r,c) in visited or grid[r][c] == "0"):
            return
        visited.add((r,c))
        self.dfs(grid, r+1,c,visited)
        self.dfs(grid, r-1,c,visited)
        self.dfs(grid, r,c+1,visited)
        self.dfs(grid, r,c-1,visited)
        