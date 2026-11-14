"""
facts:
    original arr with length n is sorted in increasing order
    and now it is rotated between 1 and n times
        -rotate n times, will have the original arr
        - nums are unique, no duplicated value
    return the minimum element of this array
    arr: 1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1 
        res = nums[0]
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
                res= min(res, nums[mid])
        return res
