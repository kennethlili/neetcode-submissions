class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        cache= {}
        def dfs(r,c):
            if r == row - 1 and c == col - 1 and obstacleGrid[r][c] == 0:
                return 1
            isoutofbound = r >= row or c >= col
            if isoutofbound or obstacleGrid[r][c] == 1:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return cache[(r,c)]
        return dfs(0,0)