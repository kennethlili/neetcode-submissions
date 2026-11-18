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
        # lookup = {}
        first = head
        while first:
            tmp = first.next 
            clone = Node(first.val)
            first.next = clone
            first.next.next = tmp
            first = tmp
        second = head
        ref = curr = Node(0)
        while second:
            curr_clone = second.next
            if second.next:
                curr_clone.next = second.next.next
            else:
                curr_clone.next = None
            if second.random:
                curr_clone.random = second.random.next
            else:
                curr_clone.random = None
            # lookup[second].next = lookup.get(second.next)
            # lookup[second].random = lookup.get(second.random)
            curr.next = curr_clone
            curr = curr.next
            second = second.next.next
        return ref.next



            



