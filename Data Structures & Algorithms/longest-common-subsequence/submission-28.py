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

time: O((m * n))
space: O((m * n))

Bound:
    i: [0,len(text1)]
    j: [0,len(text2)]

Order:
    i: big before small
    j: big before small
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text2, text1 = text1, text2
        M, N = len(text1), len(text2)
        prev = [0] * (N + 1) 

        for i in range(M - 1, -1, -1):
            curr = [0] * (N + 1) 
            for j in range(N - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
            prev = curr
        return prev[0]
