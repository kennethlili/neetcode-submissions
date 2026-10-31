# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        tmp = head
        while(tmp):
            tmp = tmp.next
            ln += 1
        k = ln - n # 0 index
        
        res = prev = ListNode()
        i = 0
        print(ln, k)
        while(head):
            print(head.val)
            nxt = head.next
            if i == k:
                prev.next = nxt
            else:
                prev.next = head
            prev = head
            head = nxt

            i+= 1
        return res.next

