# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        rev = slow.next
        while rev:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt
        slow.next = None
        list1= head
        list2 = prev


        while(list2):
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1 = tmp1
            list2 = tmp2



        

