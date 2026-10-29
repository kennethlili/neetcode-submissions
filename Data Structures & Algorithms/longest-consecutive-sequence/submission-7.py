'''
convert to set
2,20,4,10,3,5

starting n:
2, 10, 20

+1

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        start = set()
        res = 0
        for n in nums:
            numSet.add(n)
        print(numSet)
        for n in numSet:
            if (n-1) not in numSet:
                start.add(n)
        print(start)
        for n in start:
            curr = 1
            while((n + 1) in numSet):
                curr += 1
                n+=1
            res = max(res,curr)
        return res