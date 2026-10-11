class Solution:
    def rob(self, nums: List[int]) -> int:
        for n in range(len(nums)):
            if n == 1:
                nums[n] = max(nums[0], nums[1])
            elif n != 0 and n > 1:
                print(n, n-2, n-1)
                nums[n] = max(nums[n] + nums[n-2], nums[n-1])
        return nums[-1]