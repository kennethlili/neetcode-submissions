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
        lookup = {}
        res = 0
        left = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in lookup:
                left = max(left,lookup[ch] + 1)
            lookup[ch] = r
            res = max(res, r-left + 1)

        return res
                

