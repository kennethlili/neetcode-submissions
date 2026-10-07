class ListNode():
    def __init__(self,key = None,val = 0, prev = None, next = None):
        self.key  = key
        self.val = val
        self.prev = prev
        self.next =next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
    
    def pop(self,node):
        next = node.next
        prev = node.prev
        prev.next, next.prev = next, prev

    def addToTail(self,key,val):
        prev = self.tail.prev
        node = ListNode(key,val)
        self.tail.prev, prev.next = node, node
        node.prev, node.next = prev, self.tail
        return node


    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        node = self.lru[key]
        val = node.val
        self.pop(node)
        self.lru[key] = self.addToTail(key,val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.pop(node)
            self.lru[key] = self.addToTail(key,value)
        else:
            if(len(self.lru) + 1 > self.cap):
                prevnode = self.head.next
                pkey,pval = prevnode.key, prevnode.val
                self.pop(prevnode)
                del self.lru[pkey]
                self.lru[key] = self.addToTail(key,value)
            else:
                self.lru[key] = self.addToTail(key, value)


        
