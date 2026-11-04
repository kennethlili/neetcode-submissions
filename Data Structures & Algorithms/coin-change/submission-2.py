"""
Return the fewest number of coins that you need to make up the exact target amount.
If it is impossible to make up the amount, return -1.
You may assume that you have an unlimited number of each coin.

constraints:
coin size small
coin value large
target med

-take i coin -> i stay the same
-skip i coin -> i + 1

base:
    curr == amt:
        set the res (compare min)
    curr > amt:
        return
    i >= len(coins)
        return
dfs(i, target)
    take = (1 + dfs(i, target - coins[i]))
    skip = dfs(i+1, target)

O(n ^ t)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        memo = {}

        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if target == 0:
                return 0
            if i >= len(coins):
                return INF
            res = INF
            if target - coins[i] >= 0:
                res = min(res, 1 + dfs(i, target - coins[i]))
            res = min(res, dfs(i + 1, target))
            memo[(i, target)] = res
            return memo[(i, target)]

        ans = dfs(0, amount)
        return ans if ans != INF else -1
