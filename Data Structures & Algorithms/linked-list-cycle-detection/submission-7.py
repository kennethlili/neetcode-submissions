# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
facts:
    return true if have cycle, otherwise false
        at least one node can be visited again


"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head,head
        while fast and fast.next:

            fast, slow = fast.next.next ,slow.next
            if fast == slow:
                return True
        return False