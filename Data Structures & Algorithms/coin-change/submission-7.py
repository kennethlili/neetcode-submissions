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
        dp_i1 = [INF] * (amount + 1)

        for i in range(len(coins) -1, -1, -1):
            dp_i = dp_i1
            for x in range(amount + 1):
                if x == 0:
                    dp_i[x] = 0
                    continue
                dp_i[x] = min(dp_i[x], dp_i1[x])
                if x - coins[i] >= 0:
                    dp_i[x] = min(dp_i[x], 1 + dp_i[x - coins[i]])
                dp_i1 = dp_i
                
        return dp_i1[amount] if dp_i1[amount] != INF else -1
