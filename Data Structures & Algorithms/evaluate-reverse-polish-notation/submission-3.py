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
        lookup = set(['+', '-', '*', '/'])
        for token in tokens:
            isNumber = token not in lookup
            if isNumber:
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if token == '+':
                    n = n1 + n2
                elif token =='-':
                    n = n2 - n1
                elif token =='*':
                    n = n1 * n2
                else:
                    n = int(n2/ n1)
                print(n)
                stack.append(n)
        print(stack)
        return stack[0]