'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
-positive

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.
- fewest number -> min it takes to make up the target
- return -1 if cannot do it
You may assume that you have an unlimited number of each coin.
- we can take the coins multiple time
-allow duplicate

-coins len small
coin dollar amt larget
amt target med

take coins to equal to the target amt, and we can take multiple same coins

Actions:

Input: coins = coins, amount = amount

take i coins, target -> amount - coins[i] = 11 
skip i coins, target unchange

take $1 coins -> take $1 coins again or skip $1 coins and move to $5
skip i coins -> move to i + 1

time: len of coins * amt
space : len of coins * amt
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        INF = float('inf')
        def dfs(i, currSum):
            if i >= len(coins):
                return INF
            if currSum == amount:
                return 0
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            skip = dfs(i+1, currSum)
            best = skip
            if currSum + coins[i] <= amount:
                take = (1 + dfs(i, currSum + coins[i]))
                best = min(best, take)
            memo[(i,currSum)] = best
            return memo[(i,currSum)]
        res = dfs(0,0)
        return  -1 if res ==INF else res