class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minS) == 0:
            self.minS.append(val)
        else:
            currMin = self.minS[-1]
            self.minS.append(min(currMin, val))
        

    def pop(self) -> None:
        self.minS.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minS[-1]
        
