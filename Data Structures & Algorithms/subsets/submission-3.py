class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, currSet):
            if i >= len(nums):
                res.append(currSet.copy())
                return
            currSet.append(nums[i]) 
            helper(i + 1, currSet)
            currSet.pop()
            helper(i + 1, currSet)
        helper(0, [])
        return res