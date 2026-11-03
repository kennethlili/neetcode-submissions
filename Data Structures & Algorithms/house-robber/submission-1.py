"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

[2,9,8,3,6]

actions:
    -take 2 -> i + 2
    -skip2 -> i +1
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            take = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            memo[i] = max(take, skip)
            return memo[i]
        return dfs(0)
