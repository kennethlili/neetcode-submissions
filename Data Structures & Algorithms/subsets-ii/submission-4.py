"""
nums:
    may contain duplicate
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(i, curr):
            if i >= len(nums):
                res.append(curr)
                return
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                newI = i
                while newI + 1 < len(nums) and nums[newI] == nums[newI + 1]:
                    newI += 1
                numsOfDuplicated = newI - i + 1
                for k in range(1, numsOfDuplicated + 1 ):
                    helper(newI + 1, curr + [nums[i]]* k)
                helper(newI + 1, curr)
            else:
                take = helper(i + 1, curr + [nums[i]])
                skip = helper(i + 1, curr)

        helper(0, [])
        return res
