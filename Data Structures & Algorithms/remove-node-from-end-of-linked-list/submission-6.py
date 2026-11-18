# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
singly linked list
    so we can only traverse from start to removeNthFromEnd
remove nth (1th index) node from the end of the list
return the head of it
time : O(n)

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy,dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if not slow.next:
            slow.next = None
        else:
            slow.next = slow.next.next
        return dummy.next