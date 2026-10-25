class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp_i1 = [0] * (len(t) + 1)
        dp_i1[len(t)] = 1
        for i in range(len(s) - 1, -1, -1):
            dp_i = [0] * (len(t) + 1)
            dp_i[len(t)] = 1
            for j in range(len(t) - 1, -1, -1):
                dp_i[j] += dp_i1[j]
                if s[i] == t[j]:
                    dp_i[j] += dp_i1[j + 1]
            dp_i1 = dp_i

        return dp_i1[0]
