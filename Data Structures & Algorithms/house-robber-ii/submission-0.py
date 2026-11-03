"""
[2,9,8,3,6]

take 2 -> i+ 2
skip2 -> i+ 1

isFirst
 if isFirst: then we wont pick the last house
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}
        def dfs(i, isFirst):
            if (i,isFirst) in memo:
                return memo[(i,isFirst)]
            if i >= N:
                return 0
            if isFirst and i == N -1:
                return 0
            tmp = isFirst
            if i == 0:
                tmp = True
          
            take = nums[i] + dfs(i + 2, tmp)
            skip = dfs(i + 1, isFirst)
            memo[(i,isFirst)] = max(take,skip)
            return memo[(i,isFirst)]
        return dfs(0, False)

