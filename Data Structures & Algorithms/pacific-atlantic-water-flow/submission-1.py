"""
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.
    - four directions (up, down, left, or right)
    - can only go to height equal or lower

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.



Constraints:


Actions:

look thru every cell
dfs -> to check if it can reach to top left and bottom right
top left -> r <0 or c < 0 -> Pacific
bottom right -> r >= ROW, c >= COL -> Atlantic

dfs we can go 4 directions,  need to check the water
 - r+1, c
 - r- 1, c
 - r, c+ 1
 -r, c- 1
 -

"""


class Solution:
    def isPacific(self, r, c):
        if r < 0 or c < 0:
            return True
        return False

    def isAtlantic(self, r, c, ROW, COL):
        if r > ROW - 1 or c > COL - 1:
            return True
        return False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROW = len(heights)
        COL = len(heights[0])

        def dfs(r, c, res, visited):
            if r < 0 or c < 0:
                # return "Pacific"
                res[0] += 1
            if r > ROW - 1 or c > COL - 1:
                # return "Atlantic"
                res[1] += 1
            isoutofbound = self.isAtlantic(r, c, ROW, COL) or self.isPacific(r, c)
            if isoutofbound:
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                isoutofbound = self.isAtlantic(nr, nc, ROW, COL) or self.isPacific(nr, nc)

                if isoutofbound or heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc, res, visited)

            return res

        res = []
        for r in range(ROW):
            for c in range(COL):
                tmp = dfs(r, c, [0, 0], set())
                if tmp[0] > 0 and tmp[1] > 0:
                    res.append([r, c])

        return res
