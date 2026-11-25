'''
nums distinct integers
target int
reuse the same number with unlimited # of times
return the combination in any order
    but not the duplicated set
'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,curr, target):
            if target == 0:
                res.append(curr)
                return
            if target < 0 or i >= len(nums):
                return
            dfs(i,curr +[nums[i]], target - nums[i])
            dfs(i + 1,curr, target )
        dfs(0, [], target)
        return res
