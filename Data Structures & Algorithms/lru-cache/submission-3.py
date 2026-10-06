class Node:
    def __init__(self,key = None, val = 0, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail,self.head

    def pop(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def addToTail(self,key,val):
        node = Node(key,val)
        prev = self.tail.prev
        next = self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        return node
    


    def get(self, key: int) -> int:
        # move it most recent
        if(key not in self.cache):
            return -1
        copy = self.cache[key]
        self.pop(self.cache[key])
        node = self.addToTail(key,copy.val)
        self.cache[key] = node
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            copy = self.cache[key]
            self.pop(self.cache[key])
            node = self.addToTail(key,value)
            self.cache[key] = node
        else:
            if(len(self.cache) + 1 > self.cap):
                headnode = self.head.next
                hkey,hval = headnode.key, headnode.val
                self.pop(headnode)
                del self.cache[hkey]
                self.cache[key] =(self.addToTail(key, value))
            else:
                self.cache[key] =(self.addToTail(key, value))



        
