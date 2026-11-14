"""
facts:
    original arr with length n is sorted in increasing order
    and now it is rotated between 1 and n times
        -rotate n times, will have the original arr
        - nums are unique, no duplicated value
    return the target, -1 if not present
    arr: 1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        while(left <= right):
            mid = (left+ right) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[0]:
                # left to mid is sorted
                if nums[left]<=target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[0]:
                # mid to right is sorted
                print(nums[mid], nums[right])
                if nums[mid]<target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return -1
        

