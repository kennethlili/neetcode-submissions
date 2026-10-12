class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currsum = 0
        currmax = nums[0]

        currmin = 0
        mint = nums[0]
        isAllNegative = True
        for n in nums:
            if(n> 0):
                isAllNegative = False
            currsum = max(currsum, 0) + n
            currmax = max(currsum,currmax)

            currmin = min(currmin, 0) + n
            mint = min(currmin, mint)
        case1 = sum(nums) - mint
        case2 = currmax
        return max(case1, case2) if not isAllNegative else case2
