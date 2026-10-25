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
        M, N = len(word1), len(word2)
        INF = float("inf")

        memo = {}

        def dfs(i, j):
            if i >= M and j >= N:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            best = INF
            if i < M and j < N and word1[i] == word2[j]:
                best = min(best, dfs(i + 1, j + 1))
            else:
                if j < N:
                    # insert = 1 + dfs(i, j + 1)
                    best = min(best, 1 + dfs(i, j + 1))
                if i < M:
                    # delete = 1 + dfs(i + 1, j)
                    best = min(best, 1 + dfs(i + 1, j))

                if j < N and i < M:
                    # replace = 1 + dfs(i + 1, j + 1)
                    best = min(best, 1 + dfs(i + 1, j + 1))
            memo[(i, j)] = best
            return best

        return dfs(0, 0)
