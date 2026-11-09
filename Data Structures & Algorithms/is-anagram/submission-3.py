"""
s and t are anagram of each other
return true if they are, false other
anagrams -> they contains the same char, 
also the number of their appreacne must be the same, 
but order doesnt matter
s and t are at least len of 1
s and t only lower case char
s and t must be same len if they are anagrams
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s= "".join(sorted(s))
        t= "".join(sorted(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
