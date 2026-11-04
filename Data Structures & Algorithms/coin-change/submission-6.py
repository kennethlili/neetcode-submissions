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
        dp = [[INF] * (len(coins) + 1) for _ in range(amount + 1)]

       

        for i in range(len(coins) -1, -1, -1):
            for x in range(amount + 1):
                if x == 0:
                    dp[x][i] = 0
                    continue
                dp[x][i] = min(dp[x][i], dp[x][i + 1])
                if x - coins[i] >= 0:
                    dp[x][i] = min(dp[x][i], 1 + dp[x - coins[i]][i])
                
        return dp[amount][0] if dp[amount][0] != INF else -1
