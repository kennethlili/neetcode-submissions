class BrowserHistory:
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.curr = 0
        self.len = 1

    def visit(self, url: str) -> None:
        if self.curr == self.len - 1:
            self.arr.append(url)
            self.curr += 1
            self.len += 1
        else:
            self.arr[self.curr + 1] = url
            self.curr += 1
            self.len = self.curr + 1

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr = 0
            return self.arr[0]
        self.curr = self.curr-steps
        return self.arr[self.curr]

    def forward(self, steps: int) -> str:
        if(self.len <= steps + self.curr):
            self.curr = self.len -1 
            return self.arr[self.len-1]
        
        self.curr = self.curr + steps
        return self.arr[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
