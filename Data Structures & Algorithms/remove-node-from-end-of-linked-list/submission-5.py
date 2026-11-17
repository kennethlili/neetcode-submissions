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
        # m = 0
        # tmp = head
        # while(tmp):
        #     m+= 1
        #     tmp = tmp.next
        # idx = m-n
        # ref = curr= ListNode()
        # while idx:
        #     curr.next = head
        #     curr = curr.next
        #     head = head.next
        #     idx -= 1
        # curr.next = head.next
        # return ref.next
        dummy = ListNode(0, head)
        slow, fast = dummy,dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        
        