class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i,currArr, currSum):
            if(currSum > target or i >= len(nums)):
                return
            if currSum == target:
                res.append(currArr.copy())
                return
            # for n in nums:
            #     currArr.append(n)
            #     currSum += n
            #     helper(currArr, currSum)
            #     currArr.pop()
            #     currSum -= n
            n = nums[i]
            currArr.append(n)
            currSum += n
            helper(i, currArr, currSum)
            currArr.pop()
            currSum -= n
            helper(i + 1, currArr, currSum)

        helper(0,[],0)
        return res