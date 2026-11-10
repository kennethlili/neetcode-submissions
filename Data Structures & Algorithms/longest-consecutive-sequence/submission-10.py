"""
Facts:
    arr integers
        is not sorted
    consecutive seq
        exactly 1 greater than the previous element
        can be in any order, allow gaps
    0 <= arr <= 100,000
    num can be negative
    [2,20,4,10,3,4,5]
    [2,3,4,4,5,10,20]
    time: nlogn
    space = O(1)
    how do we get the consecutive sequence of nums?


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        # nums = sorted(nums)
       
        # prev = nums[0]
        # currCnt = 0
        # res = 0
        # for i in range(1, len(nums)):
        #     if nums[i] == prev + 1:
        #         currCnt  += 1
        #         res= max(currCnt, res)
        #     elif nums[i] == prev:
        #         continue
        #     else:
        #         currCnt = 0
        #     prev = nums[i]
        # return res + 1
        lookup = set(nums)
        startIndices = []
        for n in lookup:
            if (n-1) not in lookup:
                startIndices.append(n)
        res = 1
        for start in startIndices:
            n = start
            temp = 1
            while n + 1 in lookup:
                temp += 1
                res = max(res,temp)
                n += 1
        
        return res


        




