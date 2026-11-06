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
        M, N = len(text1), len(text2)
        dp = [[None] * (N + 1) for _ in range(M + 1)]

        # def lcs_at(i, j):
        #     if i == M or j == N:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + lcs_at(i + 1, j + 1)
        #     return max(lcs_at(i + 1, j), lcs_at(i, j + 1))

        for i in range(M, -1, -1):
            for j in range(N, -1, -1):
                if i == M or j == N:
                    dp[i][j] = 0
                    continue
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    continue
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
