"""
arr nums n + 1 integer, integer in nums is in the range [1,n]
only one repeated integer in nums (could be repeated multiple times), other integer appears at most once
    arr is not sorted in any order

return the repeated integer

range of the numbers are: [1,n]
contains n + 1 integer
[1,2,3,2,2]
[1,4]

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        