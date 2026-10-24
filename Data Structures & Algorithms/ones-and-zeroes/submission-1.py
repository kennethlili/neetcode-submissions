class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cntarr = []
        for string in strs:
            one = 0
            zero = 0
            for i, char in enumerate(string):
                if char == "1":
                    one += 1
                else:
                    zero += 1
                if i == (len(string) - 1):
                    cntarr.append([zero, one])

        memo = {}
        res = 0

        def dfs(i, zero, one):
            if i == len(strs):
                return 0
            if (i, zero, one) in memo:
                return memo[(i, zero, one)]
            best = dfs(i + 1, zero, one)
            cz, co = cntarr[i][0], cntarr[i][1]
            if zero - cz >= 0 and one - co >= 0:
                best = max(best , 1 + dfs(i + 1, zero - cz, one - co))
            memo[(i, zero, one)] = best
            return best

        return dfs(0, m, n)
