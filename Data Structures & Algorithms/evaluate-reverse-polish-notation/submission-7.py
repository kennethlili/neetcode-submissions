"""
an array of strings tokens that represents a valid arithmetic expression
    operations:
        plus
        minus
        times
        divide
    the arr of string are either integer or operator

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token =='-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif token =='*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif token == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(token))
       
        return stack[0]