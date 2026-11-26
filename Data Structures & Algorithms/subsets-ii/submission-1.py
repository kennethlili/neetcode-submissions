'''
nums:
    may contain duplicate
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def helper(i, curr):
            if i >= len(nums):
                res.add(tuple(curr))
                return
            take = helper(i + 1, curr + [nums[i]])
            skip = helper(i+ 1, curr)
        helper(0, [])
        return list(list(item) for item in res)


