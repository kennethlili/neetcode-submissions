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
    l: [mid, len(s)-1]
    r: [ len(s)-1, mid]

    l increasing
    r decreasing
    l -> big before small
    r: small before big

"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        S = len(s)
        prev = [0] * S 
        for l in range(S - 1, -1, -1):
            curr = [0] * S 
            for r in range(0, S, 1):
                if l > r:
                    curr[r] = 0
                    continue
                if l == r:
                    curr[r] = 1
                    continue

                if s[l] == s[r]:
                    curr[r] = 2 + prev[r - 1]
                else:
                    curr[r] = max(prev[r], curr[r - 1])
            prev = curr
        return prev[S - 1]
