"""
arr nums n + 1 integer, integer in nums is in the range [1,n]
only one repeated integer in nums (could be repeated multiple times), other integer appears at most once
    arr is not sorted in any order

return the repeated integer



"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lookup = set()
        for n in nums:
            if n in lookup:
                return n
            lookup.add(n)
        