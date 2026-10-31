# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Actions:
slow, go next
fast, go next.next

if it has cycle, slow == fast
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        slow = head.next
        fast = slow.next
        while(slow and fast):
            if fast.val == slow.val:
                return True
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
        return False
