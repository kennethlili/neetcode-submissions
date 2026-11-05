"""
Facts:

every paritition in s must be equal to some of the word from wordDict
    - no gap, no overlapping, must be completely match in string s
    - no reorder of any element provided by the questions -> 
We can reuse the word in wordDict
words in wordDict are unique
all letter are lowercase
s must be at least len 1 -> we wont have empty s
wordDict must have value and no empty string

canBreak(start):
    when start reach to the end of s:
        return True
    for end -> [start+ 1, len(s)]:
        word = s[start: end]
        if word in wordDict:
            nextCheck = canBreak(end)
            if nextCheck == True:
                return True
    return False

canBreak 0 


"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = set(wordDict)
        memo = {}
        def canBreak(start):
            if start in memo:
                return memo[start]
            if start >= len(s):
                return True
            for end in range(start+1,len(s) + 1, 1):
                word = s[start:end]
                if word in lookup:
                    nextC = canBreak(end)
                    if nextC ==True:
                        memo[start] = True
                        return memo[start]
            
            memo[start] = False
            return memo[start]
        return canBreak(0)