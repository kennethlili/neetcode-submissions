# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
actions:
loop thru all item in the list

"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for li in lists:
            copy = li
            while(copy):
                heapq.heappush(heap, copy.val)
                copy = copy.next
        res = curr = ListNode()
        while(heap):
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
        return res.next
