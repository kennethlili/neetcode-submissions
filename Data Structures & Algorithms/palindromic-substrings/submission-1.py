"""
Given a string s, return the number of substrings within s that are palindromes.

"abc"
a, b, c -> 3

"aaaaaaa"
a, a, a, aa, aa, aaa

odd:
l,r = i,i

even:
l,r = i, i+1

l-1, r+1

aaa a

1. a 0:0
2. a, aa 0:1
3. a, aa, aaa 0:2
4. a, aa, aaa, aaaa
5.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1

        return res
