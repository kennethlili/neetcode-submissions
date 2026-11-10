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
    time: nlogn -> n
    space = O(1)- > n
    how do we get the consecutive sequence of nums?


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        lookup = set(nums)
        # startIndices = []
        # for n in lookup:
        #     if (n-1) not in lookup:
        #         startIndices.append(n)
        res = 1
        for n in lookup:
            if n -1 not in lookup:
                start = n
                temp = 1
                while start + 1 in lookup:
                    temp += 1
                    res = max(res,temp)
                    start += 1

            # n = start
            # temp = 1
            # while n + 1 in lookup:
            #     temp += 1
            #     res = max(res,temp)
            #     n += 1
        
        return res


        




