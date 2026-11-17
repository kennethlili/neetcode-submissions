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


"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0
        tmp = head
        while(tmp):
            m+= 1
            tmp = tmp.next
        idx = m-n
        print(idx)
        ref = curr= ListNode()
        while idx:
            curr.next = head
            curr = curr.next
            head = head.next
            idx -= 1
        print(head.val)
        curr.next = head.next
        return ref.next
        