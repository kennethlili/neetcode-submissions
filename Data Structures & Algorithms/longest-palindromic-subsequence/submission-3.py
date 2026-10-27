'''
You are given a string s, find the longest palindromic subsequence's length in s.

bbbab
abllbla

alblblla
    l
    r
Actions:
comparing the str at l,r
shrink inward
eq:
l+1, r-1 -> +2 to the res

not eq:
    - l+1, r
    - l, r-1




base l>r
l==r

'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(l,r):
            if l>r:
                return 0
            if l == r:
                return 1
            if (l,r) in memo:
                return memo[(l,r)]
            res = 0
            if s[l] == s[r]:
                res = 2+ dfs(l+1, r-1)
            else:
                movel = dfs(l+1, r)
                mover = dfs(l, r-1)
                res = max(movel, mover)
            memo[(l,r)] = res
            return memo[(l,r)]
        return dfs(0, len(s)-1)
            
        


