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
        
        def reverse(li):
            cur = li
            canFinish = True
            for _ in range(k):
                if not cur:
                    canFinish = False
                    break
                cur = cur.next
            if not canFinish:
                return li
            prev = None
            curr = li
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt

            li.next = reverse(curr)
            return prev

        ref =res_curr= ListNode(0)
        # ref.next = reverse(head)
        curr = head
        while True:
            cur = curr
            canFinish = True
            for _ in range(k):
                if not cur:
                    canFinish = False
                    break
                cur = cur.next
            if not canFinish:
                res_curr.next  = curr
                break
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            res_curr.next = prev
            for _ in range(k):
                res_curr = res_curr.next

        return ref.next
