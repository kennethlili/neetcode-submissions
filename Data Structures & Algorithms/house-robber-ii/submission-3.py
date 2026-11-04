"""
[2,9,8,3,6]

take 2 -> i+ 2
skip2 -> i+ 1

isFirst
 if isFirst: then we wont pick the last house
"""
"""
Bounds: i:[0,N]
Order: i big before small
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            N = len(nums)
            # dp = [0] * (N+1)
            prev1 = nums[N-1]
            prev2 = 0
            for i in range(N - 2, -1, -1):
                # dp[i] = max(nums[i] + dp[i+2], dp[i+1])
                curr = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        skip1, skipEnd = nums[1:], nums[:len(nums)-1]
        return max(helper(skip1), helper(skipEnd))





