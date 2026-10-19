class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = []  # (water level, coordinate)
        added = {}  # (coordinate, water level)
        ROW, COL = len(grid), len(grid[0])

        # for r in (range(ROW)):
        #     for c in (range(COL)):
        #         if(grid[r][c] == 0):
        #             heapq.heappush(minheap, (0, (r, c)))
        #             added[(r,c)] = 0
        heapq.heappush(minheap, (grid[0][0], (0, 0)))
        added[(0,0)] = grid[0][0]
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = {}  # (coordinate, water level)

        while len(minheap) > 0 and (ROW - 1, COL - 1) not in visited:
            (waterLv, (cr, cc)) = heapq.heappop(minheap)
            visited[(cr,cc)] = waterLv
            res = max(res, waterLv)
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                isOutOfBound = nr < 0 or nc < 0 or nr >= ROW or nc >= COL

                if not isOutOfBound and (nr, nc) not in added:
                    water = grid[nr][nc]
                    heapq.heappush(minheap, (water, (nr, nc)))
                    added[(nr, nc)] = water

        return res
