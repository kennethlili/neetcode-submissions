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

        ref = curr = ListNode(0)
        ref.next = reverse(head)
        return ref.next
