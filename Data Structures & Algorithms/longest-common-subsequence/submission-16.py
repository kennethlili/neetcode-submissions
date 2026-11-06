"""
Facts:
    -subsequence, allow gaps, without changing the order -> no sorting
    - find the longest common subsequence len that exist in both text1 and text2
        - return the len
        - return 0 if no lcs
    - text1 and text2 are defined string, not empty string
    - text1 and text2 only lower case char

actions:
    if char match
        move i and j pointer by 1
    if not match
        move i
        move j

O(2^(m + n))
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def lcs_at(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[(i,j)] = (1 + lcs_at(i+1, j + 1))
            else:
                movei = lcs_at(i+1,j)
                movej = lcs_at(i, j+ 1)
                memo[(i,j)] =  max(movei, movej)
            return memo[(i,j)]
        
        return lcs_at(0,0)
            