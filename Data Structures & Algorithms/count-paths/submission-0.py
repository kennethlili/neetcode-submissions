class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row,col = m,n
        prevrow = [0] * col
        for r in range(row -1 , -1, -1 ):
            print(r)
            currrow = [0] * col
            for c in range(col -1 , -1, -1 ):
                if(c == col -1 ):
                    currrow[c] = 1
                else:
                    currrow[c] = prevrow[c] + currrow[c+1]
            print(currrow)
            prevrow = currrow
        return currrow[0]