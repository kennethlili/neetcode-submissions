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
        INF = float("inf")
        dp_i1 = [0] * (N + 1) 
       
        for i in range(M, -1,-1):
            dp_i = [0] * (N + 1) 
            
            for j in range(N, -1,-1):
                if i >= M and j >= N:
                    dp_i[j] = 0
                    continue
                dp_i[j] = INF
                if i < M and j < N and word1[i] == word2[j]:
                    dp_i[j] = min(dp_i[j], dp_i1[j+1])
                else:
                    if j < N:
                        # insert = 1 + dfs(i, j + 1)
                        dp_i[j] = min(dp_i[j], 1 + dp_i[j+1])
                    if i < M:
                        # delete = 1 + dfs(i + 1, j)
                        dp_i[j] = min(dp_i[j], 1 + dp_i1[j])

                    if j < N and i < M:
                        # replace = 1 + dfs(i + 1, j + 1)
                        dp_i[j] = min(dp_i[j], 1 + dp_i1[j+1])
            
            dp_i1 = dp_i

        return dp_i1[0]
