class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        cnt = 1
        for r in range(1, len(nums),1):
            if nums[r] == nums[r-1]:
                cnt += 1
            else:
                # reset
                cnt = 1
            if cnt <= 2:
                nums[l] = nums[r]
                l += 1
        return l

        
