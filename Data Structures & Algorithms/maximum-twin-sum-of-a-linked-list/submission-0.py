# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        # mid = slow
        prev = None
        while(slow):
            tempnext = slow.next
            slow.next = prev
            prev = slow
            slow = tempnext
        res = 0
        while(prev):
            res = max(prev.val + head.val,res)
            head, prev = head.next, prev.next
        return res