class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cntArr = []
        for st in strs:
            z, o = 0, 0
            for i, ch in enumerate(st):
                if ch == "0":
                    z += 1
                else: 
                    o += 1
                if i == len(st) - 1:
                    cntArr.append([z,o])
        
        memo = {}
        def dfs(i, zero, one):
            if i >= len(strs):
                return 0
            if (i, zero, one) in memo:
                return memo[(i, zero, one)]

            best = dfs(i + 1, zero, one)

            cz, co = cntArr[i][0], cntArr[i][1]
            if zero - cz >= 0 and one - co >= 0:
                best = max( best, 1 + dfs(i + 1, zero-cz, one - co))
            memo[(i, zero, one)] = best
            return memo[(i, zero, one)]

        return dfs(0, m,n)
