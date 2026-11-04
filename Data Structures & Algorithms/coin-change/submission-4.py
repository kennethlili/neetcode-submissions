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

Bound:
i:[0 : len(coins)]
target: [amt, 0]

i : big to small
tar: small to big
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = [[None] * (len(coins) + 1) for _ in range(amount + 1)]

        # def dfs(i, target):

        #     if target == 0:
        #         return 0
        #     if i >= len(coins):
        #         return INF
        #     res = INF
        #     if target - coins[i] >= 0:
        #         res = min(res, 1 + dfs(i, target - coins[i]))
        #     res = min(res, dfs(i + 1, target))
        #     return res
         
        for i in range(len(coins) , -1, -1):
            for x in range(amount + 1):
                if x == 0:
                    dp[x][i] =  0
                    continue
                if i >= len(coins):
                    dp[x][i] =  INF
                    continue
                res = INF
                if x - coins[i] >= 0:
                    # res = min(res, 1 + dfs(i, x - coins[i]))
                    res= min(res, 1+ dp[x-coins[i]][i])
                res = min(res, dp[x][i  + 1])
                dp[x][i] = res
        # ans = dfs(0, amount)
        return dp[amount][0] if dp[amount][0] != INF else -1
        # return 
