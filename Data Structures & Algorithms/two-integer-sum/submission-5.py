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
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == curr:
                    return [i,j]
            