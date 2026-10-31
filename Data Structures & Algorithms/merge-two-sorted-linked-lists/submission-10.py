# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = curr = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                val = list2.val
                list2 = list2.next
            else:
                val = list1.val
                list1 = list1.next
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        curr.next = list1 or list2            
        return list3.next

