# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Merge K sorted linked list
    each linked list are sorted in ascending order
return the merged linked list with sorted order

O(n*k) -> O(k+ logn)
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ref = curr = ListNode(0)
        # done = 0
        # while done != len(lists):
        #     minVal = float('inf')
        #     minIdx = None
        #     for i,li in enumerate(lists):
        #         if not li:
        #             continue
        #         minVal = min(minVal,li.val)
        #         if minVal == li.val:
        #             minIdx = i
        #     if minVal == float('inf'):
        #         break
           
        #     if not lists[minIdx].next:
        #         done += 1
        #     lists[minIdx] = lists[minIdx].next

        #     curr.next = ListNode(minVal)
        #     curr = curr.next
        # return ref.next
        ref = curr = ListNode(0)
        minArr = []
        for idx,li in enumerate(lists):
            if not li:
                continue
            heapq.heappush(minArr, (li.val, idx))
        while minArr:
            (val,idx)= heapq.heappop(minArr)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx].next:
                heapq.heappush(minArr, (lists[idx].next.val, idx))

            lists[idx] = lists[idx].next
        return ref.next


            

