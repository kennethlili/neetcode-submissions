class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.head = ListNode(0)
        self.head.next = node
        node.prev = self.head
        self.curr = self.head.next

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
        

    def back(self, steps: int) -> str:
        while(steps):
            if(self.curr.prev.val == 0):
                return self.curr.val
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while(steps):
            if not (self.curr.next):
                return self.curr.val
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)