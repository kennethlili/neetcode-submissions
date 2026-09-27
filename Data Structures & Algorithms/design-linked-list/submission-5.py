
class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

        
    def get(self, index: int) -> int:
        if(index >= self.length): 
            return -1
        curr = self.head.next
        while(index):
            curr = curr.next
            index -= 1
        return curr.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if(index > self.length):
            return None
        curr = self.head.next
        while(index):
            curr = curr.next
            index -= 1
        tempN = curr
        tempP = curr.prev
        node = ListNode(val)
        tempN.prev = node
        node.next = tempN
        tempP.next = node
        node.prev = tempP
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if(index >= self.length):
            return None

        curr = self.head.next
        while(index):
            curr = curr.next
            index -= 1
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)