lists = {
           '(': ')', '{': '}', '[' : ']'
        }

def isOpen(st):
    return st in lists
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ans = True
        for st in s:
            if isOpen(st):
                stack.append(st)
            elif len(stack) == 0:
                    return False
            else:
                lastitem = stack[-1]
                if(lists[lastitem]) != st:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
                    
