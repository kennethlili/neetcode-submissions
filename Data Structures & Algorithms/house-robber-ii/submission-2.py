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
            # memo = {}
            dp = [0] * (N+1)
            dp[N - 1] = nums[N-1]
            # def dfs(i):
                # if (i,isFirst) in memo:
                #     return memo[(i,isFirst)]
                # if i >= N:
                #     return 0
                # if isFirst and i == N -1:
                #     return 0
                # tmp = isFirst
                # if i == 0:
                #     tmp = True
            
                # take = nums[i] + dfs(i + 2, tmp)
                # skip = dfs(i + 1, isFirst)
                # return max(take,skip)

            for i in range(N - 2, -1, -1):
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
            return dp[0]
        skip1, skipEnd = nums[1:], nums[:len(nums)-1]
        return max(helper(skip1), helper(skipEnd))





