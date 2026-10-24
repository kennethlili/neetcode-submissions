class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ss = sum(stones)
        target = ss // 2
        memo = {}

        def dfs(i, currSum):
            if i >= len(stones):
                return currSum
            if currSum == target:
                return currSum
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            best = dfs(i + 1, currSum)
            if currSum + stones[i] <= target:
                best = max(best, dfs(i + 1, currSum + stones[i]))
            memo[(i, currSum)] = best
            return memo[(i, currSum)]
        
        x = dfs(0, 0 )
        print(x)
        y = ss - x
        return abs(x-y)

