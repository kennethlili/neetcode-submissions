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

time: i *j *k
space: i *j *k
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        I, J, K = len(s1), len(s2), len(s3)
        if abs(I - J) > 1:
            return False
        if I + J != K:
            return False
        memo = {}

        def dfs(i, j):
            if i >= I and j >= J:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            res = False
            k = i + j
            if i < I and s1[i] == s3[k]:
                res = dfs(i + 1, j)
            if j < J and s2[j] == s3[k]:
                res = res or dfs(i, j + 1)
        
            memo[(i, j)] = res
            return memo[(i, j)]

        return dfs(0, 0)
