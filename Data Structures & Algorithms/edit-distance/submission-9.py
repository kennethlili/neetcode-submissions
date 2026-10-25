"""
You are given two strings word1 and word2, each consisting of lowercase English letters.
    -lowercase English letters, so we dont need convert it upper case when comparing
You are allowed to perform three operations on word1 an "unlimited number of times":

Insert a character at any position ->  j+1
Delete a character at any position ->i +1
Replace a character at any position -> i+1 , j+1

Return the minimum number of operations to make word1 equal word2.

actions:

if string eq:
    move i & j pointer
if not eq
    - do all 3 case
    -
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Bound:
            i: [0, M]
            j: [0, N]
        """
        M, N = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        INF = float("inf")
       
        for i in range(M, -1,-1):
            for j in range(N, -1,-1):
                if i >= M and j >= N:
                    dp[i][j] = 0
                    continue
                best = INF
                if i < M and j < N and word1[i] == word2[j]:
                    best = min(best, dp[i+1][j+1])
                else:
                    if j < N:
                        # insert = 1 + dfs(i, j + 1)
                        best = min(best, 1 + dp[i][j+1])
                    if i < M:
                        # delete = 1 + dfs(i + 1, j)
                        best = min(best, 1 + dp[i+1][j])

                    if j < N and i < M:
                        # replace = 1 + dfs(i + 1, j + 1)
                        best = min(best, 1 + dp[i+1][j+1])
                dp[i][j] = best

        return dp[0][0]
