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

        dp_i1 = [0] * (len(t) + 1)
        dp_i1[len(t)] = 1
        for i in range(len(s) - 1, -1, -1):
            dp_i = [0] * (len(t) + 1)
            dp_i[len(t)] = 1
            for j in range(len(t) -1 , -1, -1):
                dp_i[j] += dp_i1[j]
                if s[i] == t[j]:
                    dp_i[j] += dp_i1[j + 1]
            dp_i1 = dp_i

        return dp_i1[0]
