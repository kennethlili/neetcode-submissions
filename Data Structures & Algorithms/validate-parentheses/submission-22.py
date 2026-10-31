"""
(()[{}])

"((" -> "(" -> "([{"

got the first closing bracket

{

}

{{

"""


class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char not in lookup:
                stack.append(char)
            else:
                if not len(stack):
                    return False
                opening = stack.pop()
                if lookup[char] != opening:
                    return False
        
        return len(stack) == 0
                
