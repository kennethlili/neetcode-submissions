# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        i = 0
        if len(lists) == 0:
            return None
        while i < len(lists):
            # case with odd number of len
            if i == len(lists) - 1:
                arr.append(lists[i])
            else:
                arr.append(self.merge(lists[i], lists[i + 1]))
            i += 2

        if len(lists) > 1:
            return self.mergeKLists(arr)
        else:
            return lists[0]

    def merge(self, leftArr, rightArr):
        node = ListNode()
        res = node
        while(leftArr and rightArr):
            if(leftArr.val <= rightArr.val):
                res.next = ListNode(leftArr.val)
                leftArr = leftArr.next
                res = res.next
            else:
                res.next = ListNode(rightArr.val)
                rightArr = rightArr.next
                res = res.next
        
        while(leftArr):
            res.next = ListNode(leftArr.val)
            leftArr = leftArr.next
            res = res.next
        while(rightArr):
            res.next = ListNode(rightArr.val)
            rightArr = rightArr.next
            res = res.next
        return node.next

