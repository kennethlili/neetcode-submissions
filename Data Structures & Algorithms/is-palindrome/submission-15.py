"""
find if it is palindrome
yes - True, no - False
only letters (A-Z, a-z) and numbers (0-9)
l,r

compare l and r is the same
move l and r pointer when not isalnum()

==:
move l and r
!=
return False


"  "
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r  and not s[l].isalnum():
                l += 1
            while r> l and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                print(s[l], s[r])
                return False
        return True
