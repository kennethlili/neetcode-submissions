class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        prefixmat = []
        for _ in range(ROW + 1):
            prefixmat.append([0] * (COL + 1))
        for r in range(ROW):
            pr = r + 1
            for c in range(COL):
                pc = c + 1
                val = (
                    prefixmat[pr - 1][pc]
                    + prefixmat[pr][pc - 1]
                    + matrix[r][c]  # currval
                    - prefixmat[pr - 1][pc - 1]
                )
                prefixmat[pr][pc] = val
        self.prefixmat = prefixmat

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixmat[row2 + 1][col2 + 1]
            - self.prefixmat[row2 + 1][col1 + 1 - 1]
            - self.prefixmat[row1 - 1 + 1][col2 + 1]
            + self.prefixmat[row1 + 1 - 1][col1 + 1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
