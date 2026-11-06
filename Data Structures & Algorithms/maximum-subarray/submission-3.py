class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = float('-inf')
        for i in range(0, len(nums)):
            currSum= max(nums[i],currSum+ nums[i] )
            maxSum = max(currSum, maxSum)
        return maxSum