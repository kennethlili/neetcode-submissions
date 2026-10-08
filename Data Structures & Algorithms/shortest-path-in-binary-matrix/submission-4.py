class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        if(grid[0][0] == 1 or grid[ROW-1][COL-1] == 1):
            return -1
        q.append((0,0))
        def bfs(grid):
            path = 1
            while q:
                copy = len(q)
                for i in range(copy):
                    (r,c) = q.popleft()
                    if(r == ROW -1  and c == COL -1 ):
                        return path
                    directions = [(1, 0), (1,1), (0,1), (-1, 1), (-1,0), (-1, -1), (0,-1), (1,-1)]
                    for dr, dc in directions:
                        # isoutofbound = grid[dr][dc]
                        nr, nc = r+dr, c+ dc
                        isoutofbound = nr < 0 or nc < 0 or nr >= ROW  or nc >= COL 
                        if(isoutofbound or grid[nr][nc] == 1 or (nr,nc) in visited):
                            continue
                        visited.add((nr,nc))
                        q.append((nr,nc))
                path += 1
        
        res = bfs(grid)
        if(res):
            return res
        return -1