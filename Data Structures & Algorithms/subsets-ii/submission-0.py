class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(i,currArr):
            if i >= len(nums):
                res.append(currArr.copy())
                return
            currArr.append(nums[i])
            helper(i+ 1, currArr)
            currArr.pop()

            while i+ 1 <= (len(nums) -1 ) and (nums[i] == nums[i+1]):
                i+=1
            helper(i+ 1, currArr)
        
        helper(0, [])
        return res