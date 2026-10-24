class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, currSum):
            if i == len(nums):
                if currSum == target:
                    return 1
                return 0
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            memo[(i, currSum)] = dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])
            return memo[(i, currSum)]
        return dfs(0, 0)