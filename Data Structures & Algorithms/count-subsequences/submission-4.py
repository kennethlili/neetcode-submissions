"""
You are given two strings s and t, both consisting of english letters.

Return the number of distinct subsequences of s which are equal to t.

Input: s = y, t = "xy"

s -> i
t -> j
Actions:
0:
check both i and j are eq?
equal -> dont add it to result yet -> found one x
- i + 1, j + 1 (to finish the lcs)
- i+ 1, j ( to look for another matching cases)

not equal: i+ 1, j
time: i*j
space : i*j


"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Bound:
            i: [0, len(s)]
            j : [0, len(t)]
            big to small
        """

        lcs = [[None] * (len(t) + 1) for i in range(len(s) + 1)]

        # def dfs(i, j):
        #     if j >= len(t):
        #         return 1
        #     if i >= len(s):
        #         return 0
        #     res = 0
        #     res += dfs(i + 1, j)
        #     if s[i] == t[j]:
        #         res += dfs(i + 1, j + 1)
        #     memo[(i, j)] = res
        #     return memo[(i, j)]
        
        for i in range(len(s), -1, -1):
            for j in range(len(t), -1, -1):
                if j >= len(t):
                    lcs[i][j] =  1
                    continue
                if i >= len(s):
                    lcs[i][j] =  0
                    continue
                lcs[i][j] = 0
                lcs[i][j] += lcs[i+1][j]
                if s[i] == t[j]:
                    lcs[i][j] += lcs[i+1][j + 1]
                

        return lcs[0][0]
