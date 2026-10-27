'''
Given a string s, return the longest substring of s that is a palindrome.
A palindrome is a string that reads the same forward and backward.
If there are multiple palindromic substrings that have the same length, return any one of them.

- find the longest palindromic, any of them is fine

"ababd"

"abbc"

odd:
a
bab

even:
bb
abbc

Actions:
odd:
l,r = 0,0 -> l-1, r+1

even:
l,r = i, i+1 -> l-1, r+1

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        SIZE = len(s)
        res = ""
        for i in range(len(s)):
            # odd
            l,r = i,i
            while (l>= 0 and r <= SIZE -1 and s[l] == s[r] ):
                curr = s[l:r + 1]
                if len(curr) > len(res):
                    res = curr
                l,r =   l-1, r+1
                          
            # even
            l,r = i,i+1
            while (l>= 0 and r <= SIZE -1 and s[l] == s[r]  ):
                curr = s[l:r + 1]
                if len(curr) > len(res):
                    res = curr
                l,r =   l-1, r+1
        
        return res