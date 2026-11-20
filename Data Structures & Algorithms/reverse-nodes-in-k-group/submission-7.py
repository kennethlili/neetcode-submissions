# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
singly linked list head
    only proceed forward

reverse the first k node in the linked list, and so on

if we dont have k nodes left, leave the node as it is
allow to modity the node next pointers, not the value of nodes

"""


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def canFinish(li):
            for _ in range(k):
                if not li:
                    return False
                li = li.next
            return True
        ref = res_curr = ListNode(0)
        curr = head
        while True:
            if not canFinish(curr):
                res_curr.next = curr
                break
            old_head = curr
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            res_curr.next = prev
            res_curr = old_head

        return ref.next
