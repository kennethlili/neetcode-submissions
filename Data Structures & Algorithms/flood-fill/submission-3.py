class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        self.dfs(image, sr, sc, image[sr][sc], color, set())
        return image

    def dfs(self, image, r, c, ogColor, color, visited):
        row, col = len(image), len(image[0])
        isoutofbound = r > row - 1 or c > col - 1 or r < 0 or c < 0
        print(r,c)
        if isoutofbound or image[r][c] != ogColor or (r, c) in visited:
            return False
        visited.add((r, c))
        image[r][c] = color
        self.dfs(image, r + 1, c, ogColor, color, visited)
        self.dfs(image, r - 1, c, ogColor, color, visited)
        self.dfs(image, r, c + 1, ogColor, color, visited)
        self.dfs(image, r, c - 1, ogColor, color, visited)
