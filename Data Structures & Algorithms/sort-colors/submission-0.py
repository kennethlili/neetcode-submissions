class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        obj = {
            0: 0,
            1: 0,
            2: 0
        }
        for n in nums:
            obj[n] += 1
        i = 0
        for key, val in obj.items():
            for j in range(val):
                nums[i] = key
                i+=1
                