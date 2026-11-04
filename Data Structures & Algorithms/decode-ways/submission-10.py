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

time: O(2^n)

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)
        lookup = set()
        for n in range(1, 27, 1):
            lookup.add(str(n))
        memo = {}
        def dfs(i, digit):
            if (i,digit) in memo:
                return memo[(i,digit)]
            if digit not in lookup:
                return 0
            if i >= S and digit in lookup:
                return 1
            
            res = 0
            res += dfs(i+1, s[i])
            if i+1 < S:
                res += dfs(i+2, s[i: i+2])
            memo[(i,digit)] = res
            return memo[(i,digit)]

        return dfs(0, s[0])