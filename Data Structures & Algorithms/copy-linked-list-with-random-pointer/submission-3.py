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
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        first = head
        while first:
            tmp = first.next
            clone = Node(first.val)
            first.next = clone
            first.next.next = tmp
            first = tmp
        second = head
        while second:
            curr_clone = second.next
            if second.random:
                curr_clone.random = second.random.next
            else:
                curr_clone.random = None
            second = second.next.next
        # third = head.next
        # while third:
        #     third.next = third.next.next
        #     third = third.next.next
        # return head
        curr = head
        cloned_head = head.next
        while(curr):
            clone = curr.next
            curr.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            else:
                clone.next = None
            curr = curr.next
        return cloned_head



