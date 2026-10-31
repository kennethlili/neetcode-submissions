# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = [None]
        if not lists: 
            return None
        def helper(lists):
            if len(lists) == 1:
                res[0] = lists[0]
                return
            newLists = []
            for i in range(0, len(lists), 2):
                li = lists[i+1] if i + 1 < len(lists) else None
                merged = self.merge2Lists(lists[i], li)

                newLists.append(merged)
            helper(newLists)
        helper(lists)
        return res[0]
            


        
            
    def merge2Lists(self, list1, list2):
        res = curr = ListNode()
        while(list1 and list2):
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
        return res.next
     