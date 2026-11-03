"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

[2,9,8,3,6]

actions:
    -take 2 -> i + 2
    -skip2 -> i +1

Bound:
i : [0, len(nums)]

big before small

"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # dp = [0] * (N + 1)
        # dp[N - 1] = nums[N - 1]
        prev2 = 0
        prev1 = nums[N - 1]

        for i in range(N - 2, -1, -1):
            curr = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
