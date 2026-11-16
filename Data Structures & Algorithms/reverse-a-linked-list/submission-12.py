# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
facts:
    head (beginning)
        singly linked list
    reverse the linked list
    return the new beginning
"""


class Solution:
    def reverseList(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev,curr = curr,nxt
        return prev
