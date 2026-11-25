"""
nums contains unique intergers
return all possible subsets of nums
    return in any order
no duplicate subsets
    [1,2] and [2,1] are duplicate

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, curr):
            if i >= len(nums):
                copy = curr.copy()
                res.append(copy)
                return
            skip = helper(i + 1, curr)
            curr.append(nums[i])
            take = helper(i + 1, curr)
            curr.pop()
            return 

        helper(0, [])
        return res
