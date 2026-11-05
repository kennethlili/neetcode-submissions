"""
Facts:
    - the nums are not sorted, we cannot sort it as we need to retain the orginal order
    - increasing subsequence doesnt have to be +1, as long as nums[i] < nums[j], then it is valid
    - duplicate element exist in nums
    - gaps allowed
    - return the max len of the LIS
    - nums >= 1, so we have output as 1 in minimum
    
    - nums[i] contains negative numbers
Brute Force:
lis_from(i)
    best = 1
    for j in range(i+1,len(nums),1):
        if nums[j] > nums[i]:
            best = max(res, 1+ lis_from(j))
    return best
return max(lis_from(i) for i in range(n))

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        memo = {}
        def lis_from(i):
            if i in memo: return memo[i]
            best = 1
            for j in range(i+ 1,n, 1):
                if nums[j] > nums[i]:
                    best = max((1 + lis_from(j)),best)
            memo[i] = best
            return best
        for i in range(n):
            res = max(lis_from(i), res)
        return res
