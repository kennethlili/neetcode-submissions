class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # leftarr=[]
        rightarr = [0] * len(nums)
        leftcurr = 1
        rightcurr = 1
        res = []
        for i in range(len(nums) -1 , -1, -1):
            val = nums[i] * rightcurr
            rightarr[i] = val
            rightcurr = val
        for i in range(len(nums) ):
            if i == 0:
                res.append(rightarr[1])
            elif i == len(nums) -1:
                res.append(leftcurr)
            else:
                res.append(rightarr[i+1] * leftcurr)
            val = nums[i] * leftcurr
            # leftarr[i] = val
            leftcurr = val
        return res

            

        