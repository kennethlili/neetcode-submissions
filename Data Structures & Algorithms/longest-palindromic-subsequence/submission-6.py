"""
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

time: l x r
l<n
r < n
Bounds:
    l: [0, len(s)-1]
    r: [0, len(s)-1]

    l increasing
    r decreasing
    l -> big before small
    r: small before big

"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        dp = [[0] * (len(s)) for _ in range(len(s))]
        # for l in range(len(s) - 1, -1, -1):
        #     dp[l][l] = 1
        for l in range(len(s) - 1, -1, -1):
            for r in range(0, len(s), 1):
                if l > r:
                    dp[l][r] = 0
                    continue
                if l == r:
                    dp[l][r] = 1
                    continue
                res = 0
                if s[l] == s[r]:
                    res = 2 + dp[l + 1][r - 1]
                else:
                    movel = dp[l + 1][r]
                    mover = dp[l][r - 1]
                    res = max(movel, mover)
                dp[l][r] = res
        return dp[0][len(s) - 1]
