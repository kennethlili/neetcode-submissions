'''
You are given a string s, find the longest palindromic subsequence's length in s.

bbbab
abllbla

alblblla
    l
    r
Actions:
comparing the str at l,r
eq:
l-1, r+1 -> +1 to the res

not eq:
    -l-1, r
    -l, r+1


odd: l,r = i,i
even: l,r = i,i+1

base l <0 or r> len(s) -1

'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(l,r):
            if  l <0 or r> len(s) -1:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            res = 0
            if s[l] == s[r]:
                if l == r:
                    res = 1+ dfs(l-1, r+1)
                else:
                    res = 2+ dfs(l-1, r+1)
            else:
                movel = dfs(l-1, r)
                mover = dfs(l, r+1)
                res = max(movel, mover)
            memo[(l,r)] = res
            return memo[(l,r)]
        ans = 0
        for i in range(len(s)):
            odd = dfs(i,i)
            even = dfs(i,i+1)
            ans = max(ans,odd,even)
        return ans


