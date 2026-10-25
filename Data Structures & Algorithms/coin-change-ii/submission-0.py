'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
- dollar must be postive integer
- amount must be postive integer

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.
- distinct combination
- return 0 if impossible

You may assume that you have an unlimited number of each coin and that each value in coins is unique.
- coins val is unique
- we can pick same coins again

- coins length mid
- coins val large
- amt target large

we need to pick different val in coins arr, to reach the target val, and we can pick the same nums on each terms

Input: amount = 4, coins = [1,2,3]
actions:
pick i -> pick i again/ skip i (i+1)
skip i(i+1) -> 

check if target < 0 -> return 0, == 0 -> return 1


'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i,target):
            if target < 0 or i>= len(coins):
                return 0
            if target == 0:
                return 1
            if (i,target) in memo:
                return memo[(i,target)]
            # for coin in coins:
            #     res += dfs(target - coin)
            take = dfs(i, target- coins[i])
            skip = dfs(i+1, target)
            memo[(i,target)] = take + skip
            return memo[(i,target)]
        return dfs(0,amount)






            