# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
2,4,6,8
0,1,2,3 n =4

2,8,4,6




2,4,6, 8<-10 mid = 3

2,10,4,8,6

Actions:
    head, tail
    set head -> tail -> head -> 

    find the tail
    on each iteration, we go next.next
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        isMid = False
        rev = None
        n = 0
        while(slow):
            if not fast.next or not fast.next.next:
                isMid = True
            curr = ListNode(slow.val)
            curr.next = rev
            rev = curr
            slow = slow.next
            if not isMid:
                fast = fast.next.next
            n +=1
        dummy = ListNode()
        res =  dummy
        # while(rev):
        #     print(rev.val)
        #     rev = rev.next
        newHead = head
        for i in range(n):
            new = i + 1
            # even
            if not (new % 2 ): 
                print(rev.val, 'rev')
                dummy.next = ListNode(rev.val)
                dummy = dummy.next
                rev = rev.next
            else:
                print(newHead.val, 'newHead')

                dummy.next = ListNode(newHead.val)
                dummy = dummy.next
                newHead = newHead.next
        node, cur = head, res.next
        while node and cur:
            node.val = cur.val
            node = node.next
            cur = cur.next


