"""
facts:
    string s
    return the len of longest substring without duplicate char
    substring contiguous sequence of characters within a string
        no gaps
    string s 
        0 <= s.length <= 50,000

time O(n^2)
space: O(n)

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        
        lookup = {} # key=char, val: index
        l, r = 0, 0
        while r < len(s):
            if s[r] in lookup:
                l = max(l,lookup[s[r]] + 1)
                
            res = max(res, r-l +1)
            lookup[s[r]] = r
            r+= 1
        return res
# for i, ch in (enumerate(s)):
        #     lookup = set(ch)
        #     currRes = 1
        #     find the max len substring without duplicate char
        #     for j in range(i+1, len(s)):
        #         if s[j] in lookup:
        #             break
        #         currRes = j - i + 1
        #         lookup.add(s[j])
        #     res = max(currRes, res)
        # return res



                
