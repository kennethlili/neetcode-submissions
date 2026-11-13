"""
facts:
    nums are sorted in increasing order, no duplicated numbers
    return the index of target, if not exist, then return -1
    run in O(logn)
    arr 1 <= nums.length <= 10000
    nums can be negative
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            print(mid, nums[mid])
            if nums[mid] < target:
                # pick right
                left = mid + 1
            elif nums[mid] > target:
                # pick left
                right = mid -1
            else:
                return mid
        return -1