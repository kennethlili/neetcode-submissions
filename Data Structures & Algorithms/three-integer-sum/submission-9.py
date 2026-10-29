'''
[-1,0,1,2,-1,-4]

[-4|,-1,-1,-1,0,1,2]


-1 -1 2
-1 0 1

actions:
-4, tar -> 0-)-4) = 4
-1 , tar = 1

l ,r

increae l to increase the target
dont move the same number

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            
            l, r= i + 1, len(nums) - 1
            if i != 0 and nums[(i-1)] == nums[i]:
                continue
           
            while l <r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while(l < r ) and nums[l] == nums[l- 1]:
                        l +=1
                    while(l < r ) and nums[r] == nums[r + 1]:
                        r -=1
                    continue

               
                if s < target:
                    l += 1
                    continue
                if s > target:
                    r  -= 1
                    continue
                
        return res
            
        
            
 