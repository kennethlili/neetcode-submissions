# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
iterate both link list
while list1 and list2:

check list1 
check list2 is defined

if list1 < list2
    set to list1
else:
    set to list2
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = curr = ListNode()
        while list1 and list2:

        # check list1 
        # check list2 is defined
            node = None
            if list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            
            curr.next = node
            curr = node
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        return prev.next
            