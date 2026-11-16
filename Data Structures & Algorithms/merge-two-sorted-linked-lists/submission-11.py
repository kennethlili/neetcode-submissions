# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
head of two linked list
    both of them are sorted
merge them into one sorted linked list and return the head

"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        ref = curr
        while(list1 and list2):
            if list1.val >= list2.val:
                val = list2.val
                list2 = list2.next
            else:
                val= list1.val
                list1 = list1.next
            node = ListNode(val)
            curr.next = node
            curr= curr.next
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        return ref.next
