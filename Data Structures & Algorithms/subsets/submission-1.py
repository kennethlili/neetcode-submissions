class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def helper(n):
            resCopy = res[::]
            for arr in resCopy:
                copy = arr[::]
                copy.append(n)
                res.append(copy)

            # print(res)
                

        i = 0
        while(i < len(nums)):
            print(nums[i])
            helper(nums[i])
            i+=1
        return res
      
            

                
