class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        dic = {}
        main = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            dic[char] = dic.get(char, 0) + 1
            main = max(main, dic[char])
            while r - l + 1 - main > k:

                dic[s[l]] -= 1        
                l+= 1
            res = max( r-l + 1, res)
        return res

