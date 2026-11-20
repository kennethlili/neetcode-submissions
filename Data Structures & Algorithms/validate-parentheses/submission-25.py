"""
s consist of '(', ')', '{', '}', '[' and ']'
    string is not sorted
    s length 1 <= s.length <= 1000
    s must be even number
string is valid only if:
    open match the same type of close bracket
    open close in the correct order
    close bracket has a corresponding open bracket of the same type.
return True if s is valid, false otherwise
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # close to open
        lookup = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for ch in s:
            isClose = ch in lookup
            if not isClose:
                stack.append(ch)
            else:
                if not stack or stack[-1] != lookup[ch]:
                    return False
                last = stack.pop()
        
        return (len(stack) == 0) 
