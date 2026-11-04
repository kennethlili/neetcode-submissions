"""
find the largest product of a subarr in nums
Constraints:
nums len large
nums[i] contains negative number, and bounded by -10 to 10

actions:
keep track of curr max and min

res:
currMax: compare the currMax * n,n, currMin * n
currMin:currMin*n,n,currMax * n


"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        INF = float('inf')
        NINF = float('-inf')
        res = NINF
        currMax, currMin = 1, 1
        for n in nums:
            tmpmax, tmpmin = currMax, currMin
            currMax = max(tmpmax * n, n, tmpmin *n)
            currMin = min (tmpmax * n, n, tmpmin *n)
            res = max(res, currMax)
        return res