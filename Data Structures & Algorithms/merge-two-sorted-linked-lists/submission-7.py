# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while(list1 and list2):
            list1Val = list1.val
            list2Val = list2.val
            if(list1Val> list2Val):
                tail.next = list2
                list2 = list2.next
                tail = tail.next
            else: 
                tail.next = list1
                list1 = list1.next
                tail = tail.next
        tail.next = list1 or list2

        return dummy.next