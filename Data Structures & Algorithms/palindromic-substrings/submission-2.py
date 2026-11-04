"""
aaa

i = 0,
a

i = 1,
a, a, aaa

i = 2,
a, a ,a , aa, aa, aaa
1, 1, 1,, 

brute force:
a , a, a
aa, aa
aaa

DP implementation:
    -odd, l = i, r= i
    -even, l = i, r= i+1
    expand the l and r if str l == str r, add to the res meanwhile
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        S =len(s)
        for i in range(S):
            # odd
            l,r = i,i
            while l >= 0 and r <= S -1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # even
            l,r = i,i+1
            while l >= 0 and r <= S -1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res
        