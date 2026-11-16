# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
reorder length = 7 linked list
    singly-linked, we can only move forward

[0, 1, 2, 3, 4, 5, 6]
->
[0, 6, 1, 5, 2, 4, 3]
[0, n-1, 1, n-2, 2, n-3, ...]
we cannot modify the values in the list node


[2,4,6,]

[10,8,]

len
5 -> 3
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        if not slow.next:
            return
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        rev = slow.next
        slow.next = None
        while rev:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt

        curr = head
        while prev:
            tmp1, tmp2 = curr.next, prev.next
            curr.next = prev
            prev.next = tmp1
            curr = tmp1
            prev = tmp2

        # head = ref
