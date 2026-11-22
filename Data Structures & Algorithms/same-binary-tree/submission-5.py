# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
p and q
return true if the tree are equivalent, return False otherwise
equivalent -> they share the exact same strcuture and nodes that has the same value
    same structure -> same left, same right (they exist)
    same value -> left.val == left.val, same for right side


"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP = deque([p])
        queueQ = deque([q])
        
        while queueP and queueQ:
            pNode = queueP.popleft()
            qNode = queueQ.popleft()

            if not pNode and not qNode:
                continue
            if not pNode or not qNode or pNode.val != qNode.val:
                return False

            queueP.append(pNode.left)
            queueQ.append(qNode.left)
            queueP.append(pNode.right)
            queueQ.append(qNode.right)

        return True
