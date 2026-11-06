"""
Facts:
    the nums is not sorted
    find the subarray with largest sum
        - non-empty
        - contiguous, no gaps
        - relative order matter, sorting is not allowed at first glance
    return the sum
    nums bounded by 1 and 100,000
        - output must present
        - nlogn more prefer or faster
    nums[i] contains negative number

Brute Force:
    res = -INF
    for i in range(len(nums)):
        for j in range(i+1, len(nums),1):

O(n^2)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        M = len(nums)
        cuma = 0
        for i in range(M):
            if cuma  < 0:
                cuma = 0
            cuma += nums[i]
            res = max(res,cuma)
        
        return res