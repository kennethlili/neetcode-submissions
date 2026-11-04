"""
Actions:

odd case: l,r => i, i
even case: l,r => i, i +1

iteration: out of bound case
l <0 r > len(s)
l -= 1
r += 1

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        S = len(s)
        for i in range(S):
            # odd
            l,r = i,i
            while l>=0 and r<= S-1 and s[l] == s[r]:
                ln = r - l + 1
                if ln > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # even
            l,r = i,i+1
            while l>=0 and r<= S-1 and s[l] == s[r]:
                ln = r - l + 1
                if ln > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res