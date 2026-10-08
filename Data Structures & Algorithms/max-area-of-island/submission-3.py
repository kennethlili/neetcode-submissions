class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            isOoB = r < 0 or c < 0 or r > ROW - 1 or c > COL - 1
            if isOoB or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    res = max(area, res)

        return res
