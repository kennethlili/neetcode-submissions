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
        queue = deque([p, q])
        while queue:
            pNode = queue.popleft()
            qNode = queue.popleft()
           
            if not pNode and not qNode:
                continue
            if not pNode or not qNode or pNode.val != qNode.val:
                return False
            
            queue.append(pNode.left)
            queue.append(qNode.left)
            queue.append(pNode.right)
            queue.append(qNode.right)
        
        return True