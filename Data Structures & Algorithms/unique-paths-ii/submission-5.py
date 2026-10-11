class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row,col = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * col
        isBlock = False ## indiciate last col blocked or not
        for r in range(row -1 , -1, -1):
            curr = [0] * col
            for c in range(col -1 , -1, -1):
                print(row,col)
                print(r,c)
                val = obstacleGrid[r][c]
                if c == col -1:
                    isBlock = isBlock or val == 1
                    curr[c] = 0 if isBlock else 1
                else:
                    if val == 1:
                        curr[c] = 0
                    else:
                        curr[c] = prev[c] + curr [c+1]
            prev = curr
        return prev[0]