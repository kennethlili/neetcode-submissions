"""
facts:
    return true if s is palindrome, otherwise false
    palindrome reads the same forward and backward
        - case insensitive
        - ignore non alphanumeric char
    1 <= s.length <= 1000     
    s is made up of only printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        while(l< r):
            # edge ".a"
                #    l  r
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

           
            
        