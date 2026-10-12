class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charmap = {}
        l = 0
        for r in range(len(s)):
            if s[r] in charmap and charmap[s[r]] >= l:
                # charmap[s[r]] = 
                l = charmap[s[r]] + 1
            charmap[s[r]] = r
           
            k = r - l + 1
            res = max(res, k)

        return res
