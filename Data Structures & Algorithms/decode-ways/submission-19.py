"""
lookup
actions:
"41012"
take4 -> take 1/ take 10 -> i + 1
41 -> take0/ take 02 -> i +2,

path:
take i th index, i+1, check i
take i+1 index and add to i, i+2, if (i+1 ) out of bound => i+1 < len(s)
check i->i+1

bse case:
if we reach to len(s), return 1
if digit not in lookup, return 0

dfs(i,digit)

time: O(2^n) -> n

Bound:
    i: [0, S]
    i ++ -> big before small
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        lookup = set()
        for n in range(1, 27, 1):
            lookup.add(str(n))
        
        S = len(s)
        prev2 = 1
        prev1 = 0
        if s[S - 1] in lookup:
            prev1 = 1
        for i in range(S - 2, -1, -1):
            res = 0
            if s[i] in lookup:
                res += prev1
            if s[i : i + 2] in lookup:
                res += prev2
            prev2 = prev1
            prev1 = res
        return prev1
