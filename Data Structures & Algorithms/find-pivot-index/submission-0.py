class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightarr = [0] * (len(nums) )
        rightcurr = 0

        leftcurr = 0
        for i in range(len(nums) -1 , -1, -1):
            rightarr[i] = nums[i] + rightcurr
            rightcurr = nums[i] + rightcurr
        for (i, n) in enumerate(nums):
            curr = nums[i] + leftcurr
            leftcurr = curr
            if curr == rightarr[i]:
                return i
        return -1
            