class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        ROW, COL = len(grid), len(grid[0])
        fresh = 0
        min = 0
        for r in range(ROW):
            for c in range(COL):
                val = grid[r][c]
                if val == 1:
                    fresh += 1
                elif val == 2:
                    queue.append((r, c))
        if fresh == 0:
            return 0
        if len(queue) == 0:
            return -1
        while queue:
            copy = len(queue)
            if fresh == 0:
                return min
            for i in range(copy):
                r, c = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    isoutofbound = nr < 0 or nc < 0 or nr > ROW - 1 or nc > COL - 1
                    if isoutofbound or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1

            min += 1

        print(fresh)
        if fresh != 0:
            return -1
        return min
