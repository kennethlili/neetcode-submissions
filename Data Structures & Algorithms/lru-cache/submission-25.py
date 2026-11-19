"""
LRUCache(int capacity) -> init with capacity
get -> get the key if exist, otherwise -1
    A key is considered used when we get it
    run in O(1) time

    find the node in any position and pop it and put the node at the end

put -> overwrite the key if exist, other just add the key-val pair
    if exceed the capacity, remove the least recently used key
    A key is considered used when we put it
    run in O(1) time

    within the cap:
        put the node at the end
    exceed:
        pop the node at the start and put the node at the end
"""


class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}  # key: key, val: node
        self.length = 0

    def addToTail(self, key, val):
        node = ListNode(key, val)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail
        return node

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # prev = node.prev
        # nxt = node.next
        # prev.next = nxt
        # nxt.prev = prev
        self.removeNode(node)
        self.cache[key] = self.addToTail(key, node.val)

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.length += 1
            self.cache[key] = self.addToTail(key, value)
            if self.length > self.capacity:
                node = self.head.next
                removeKey = node.key
                self.removeNode(node)
                self.length -= 1
                del self.cache[removeKey]
        else:
            node = self.cache[key]
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            self.cache[key] = self.addToTail(key, value)
