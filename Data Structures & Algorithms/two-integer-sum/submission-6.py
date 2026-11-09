"""
Facts:
    we need to find the nums[i] + nums[j] == target
        we cannot use same i and j -> we cannot reuse the same elements in the arr
    there must be exactly one pair of i and j that satify the condition
    return the smaller index first
    there is not guartne that the arr is sorted
    2 <= nums.length <= 1000 
    num[i] can be negative
    target can be negative

    time: O(n^2)
    space: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # key: val, val: index
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in lookup:
                return [lookup[curr], i]
            lookup[nums[i]] = i
            # # we look for any nums in j that == curr
            # for j in range(i+1, len(nums)):
            #     if nums[j] == curr:
            #         return [i,j]

            