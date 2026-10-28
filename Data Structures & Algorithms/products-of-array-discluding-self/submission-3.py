'''
nums large
num small, but has negative -> no arr indexing

[1,2,4,6]
[1,1, 2, 8]
[   48 ,24,6,1]

[48, 24, 12, 8]

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixR = [1] * len(nums)
        currP = 1
        currPR = 1
        res= [] 

        for i in range(len(nums)-1, -1, -1):
            prefixR[i] = currPR
            currPR = nums[i] * currPR
        for i in range(len(nums)):
            res.append(currP * prefixR[i])
            currP = nums[i] * currP
        return res
        
