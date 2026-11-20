"""
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
    push the val at the end
void pop() removes the element on the top of the stack.
    rmove the element at the end
int top() gets the top element of the stack.

int getMin() retrieves the minimum element in the stack.

stack
minStack
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = val if not self.minStack else min(self.minStack[-1], val)
        if not self.minStack:
            self.minStack.append(minVal)
        elif val <= self.minStack[-1]:
            self.minStack.append(minVal)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
