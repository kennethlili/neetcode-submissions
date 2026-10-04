class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, arr, sum):
            if(i >= len(nums)):
                return
            if sum == target:
                res.append(arr)
                return 
            if sum> target:
                return
            num = nums[i]
            
            copy = arr[::]
            copy.append(num)
            dfs(i,copy,sum+num)

            dfs(i+1, arr, sum)
        
        dfs(0, [], 0)
        return res