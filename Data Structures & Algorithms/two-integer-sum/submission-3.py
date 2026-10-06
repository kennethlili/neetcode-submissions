class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            n = nums[i]
            
            tnum = target - n
            if tnum in map:
                return [map[tnum][0], i]
            if n not in map:
                map[n] = [i]
            else:
                map[n].append(i)
                    