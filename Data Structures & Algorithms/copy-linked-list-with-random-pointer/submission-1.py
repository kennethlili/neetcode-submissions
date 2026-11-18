"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
linked list with n new Node:
    each node will have the val, next,random
        val: original val
            not guaranteed to be unique
        next: pointing to the next pointer
        random: pointing to a random pointer
            could be any node/ null
return a deep copy to the head



"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        lookup = {}
        first = head
        while first:
            node = Node(first.val)
            lookup[first] = node
            first = first.next
        second = head

        while second:
            lookup[second].next = lookup.get(second.next)
            lookup[second].random = lookup.get(second.random)
            second = second.next
        return lookup[head]



            



