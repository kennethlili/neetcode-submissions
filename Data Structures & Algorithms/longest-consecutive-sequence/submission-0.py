class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsCnt = {}
        for n in nums:
            numsCnt[n] = 1
        res = 0
        for n,_ in numsCnt.items():
            if n -1 not in numsCnt:
                length = 1
                curr = n
                while curr + 1 in numsCnt:
                    length += 1
                    curr += 1
                res = max(length,res)
        return res