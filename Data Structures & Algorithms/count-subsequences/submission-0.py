'''
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
'''
    

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            movei = dfs(i+ 1, j)
            res += movei
            if s[i] == t[j]:
                moveboth = dfs(i+1, j+1)
                res += moveboth
            memo[(i,j)] = res
            return memo[(i,j)]
        return dfs(0,0)