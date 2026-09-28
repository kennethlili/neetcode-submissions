class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        print(self.q)

    def pop(self) -> int:
        length = len(self.q)
        ans = 0
        while(length):
            if(length == 1):
                ans = self.q.popleft()
            else:
                n = self.q.popleft()
                self.push(n)
            length -= 1
        return ans

    def top(self) -> int:
        return self.q[len(self.q)-1]


    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()