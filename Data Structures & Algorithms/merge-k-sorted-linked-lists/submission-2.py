# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists):
            return None
        arr = []
        i = 0
        while i < len(lists):
            # handle the case for odd number
            if(i+ 1 == len(lists)):
                arr.append(lists[i])
            else:
                arr.append(self.merge(lists[i], lists[i+1]))
            i +=2

        if(len(lists) == 1):
            return lists[0]
        else:
            return self.mergeKLists(arr)

    def merge(self,left,right):
        dummy = ListNode()
        curr = dummy
        while(left and right):
            if left.val <= right.val:
                curr.next = ListNode(left.val)
                left = left.next
                curr = curr.next
            else:
                curr.next = ListNode(right.val)
                right = right.next
                curr = curr.next
            
        while(left):
            curr.next = ListNode(left.val)
            left = left.next
            curr = curr.next
            
        while(right):
            curr.next = ListNode(right.val)
            right = right.next
            curr = curr.next

        return dummy.next


        