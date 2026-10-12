class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charmap = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in charmap:
                charmap[s[r]] = 0
            charmap[s[r]] += 1
            while(charmap[s[r]] > 1):
                charmap[s[l]] -= 1
                l += 1
            k = r-l + 1
            res = max(res, k)
        
        return res
