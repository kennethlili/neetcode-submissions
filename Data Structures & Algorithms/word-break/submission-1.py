"""
use wordDict to form s
    -we can use reuse the wordDict
    -wordDict unique
    - we dont have to use all the wordDict

Constraints:
    string small
    workDict length small
    str in wordDict is small

wordDict arr -> set()

applepenapple

apple pen apple

applepen

catsincars

cat
cats

actions:
loop thru the char in s
if curr in wordDict
    -include the word -> reset the curr to 'r' -> 

-not to include it -> continue the count
add the curr len, if total add up res == s -> return True
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = set(wordDict)
        memo = {}
        def dfs(i, curr):
            if (i,curr) in memo:
                return memo[(i,curr)]
            if i >= len(s):
                if curr in lookup:
                    return len(curr)
                return 0
            
            # skip
            res = dfs(i + 1,curr + s[i])
            if curr in lookup:
                take = (len(curr) + dfs(i+1, s[i]))
                res = max(take, res)
            memo[(i,curr)] = res
            return memo[(i,curr)]
        return dfs(0, "") == len(s)
            
