class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = []  # (water level, coordinate)
        ROW, COL = len(grid), len(grid[0])

        heapq.heappush(minheap, (grid[0][0], (0, 0)))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set((0,0))  # (coordinate, water level)

        while minheap:
            (waterLv, (cr, cc)) = heapq.heappop(minheap)
            if cr == ROW -1 and cc == COL -1:
                return waterLv
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                isOutOfBound = nr < 0 or nc < 0 or nr >= ROW or nc >= COL

                if not isOutOfBound and (nr, nc) not in visited:
                    water = grid[nr][nc]
                    heapq.heappush(minheap, (max(waterLv,water), (nr, nc)))
                    visited.add((nr,nc))

        return res
