class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        numsMap = {}
        while r < len(nums):
            n = nums[r]
            if(abs(l-r) > k):
                numsMap.pop(nums[l])
                # del numsMap[nums[l]]
                l += 1
            if(n in numsMap):
                return True
            numsMap[n] = 0
            r += 1
        return False