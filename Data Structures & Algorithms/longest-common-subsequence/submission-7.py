'''
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.
- get the lcs
- return 0 if not exist

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".

A common subsequence of two strings is a subsequence that exists in both strings.

summary: get lcs of 2 texts
-both texts are defined, so we dont need to check edge case where text1 or text2 doesnt have anything
- text1 and text2 consist of only lowercase English characters.
    - we just need to ==, no need any converation

Input: text1 = "cat", text2 = "crabt" 


Actions:
text1 - > i, text2 -> j
i = 0, j = 0 ->they are equal -> +1 -> add both i and j pter
i = 1, j= 1 -> != 
-> keeping i constant, increase j
-> keeping j constant, increase i

found -> increase i and j
not found, 

base case: 
if anyone of the pter out of bound (len(text)) -> return
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            best = 0
            if text1[i] == text2[j]:
                best = (1 + dfs(i + 1, j+ 1))
            else:
                movei = dfs(i + 1, j)
                movej = dfs(i, j+ 1)
                best = max(movei, movej)
            memo[(i,j)] =  best
            return memo[(i,j)]
        return dfs(0,0)

            

        