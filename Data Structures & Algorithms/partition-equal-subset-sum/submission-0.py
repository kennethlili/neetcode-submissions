class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su % 2 != 0:
            return False

        
        def dfs(i, target):
            if target == 0:
                print('found')
                return True
            if target < 0:
                return False
            if i  == len(nums):
                return False
            if dfs(i + 1, target - nums[i]) or dfs(i + 1, target):
                return True
            return False
            

        
        if dfs(0, su/2) == True:
            return True
        return False
