"""
You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.
 - return true / false

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

You may assume that s1, s2 and s3 consist of lowercase English letters.
    - lowercase only

- check s1 and s2 the len diff is <= 1
- check len of s1 + s2 = len of s3

Input: s1 = "aaaa", s2 = "abbbb", s3 = "aaabbbbaa"
s1 -> i
s2 -> j
s3 -> k
actions:
check if
s3[k] == s1[i] -> i+1, k +1
s3[k] == s2[j] -> j+1, k +1
# s3[k] == s1[i] and s3[k] == s2[j] ->i+1, k +1 / j+1, k +1
if not eqal to any one of s1 or s2 return False

base case:
    if all pointer at the end, return True, otherwise False

time: i *j
space: i *j

"""

"""
Bounds: 
    i : [0, lens1]
    j : [0, lens2]
    big to small
    [0,0,0,0]
    J should be smaller

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        I, J, K = len(s1), len(s2), len(s3)
        if I + J != K:
            return False
        prev = [False] * (J + 1) 
        for i in range(I, -1, -1):
            curr = [False] * (J + 1) 
            if i == I:
                curr[J] = True
            for j in range(J, -1, -1):
                k = i + j
                if i < I and s1[i] == s3[k]:
                    curr[j] = prev[j]
                if j < J and s2[j] == s3[k]:
                    curr[j] = curr[j] or curr[j + 1]
            prev = curr
        return prev[0]
