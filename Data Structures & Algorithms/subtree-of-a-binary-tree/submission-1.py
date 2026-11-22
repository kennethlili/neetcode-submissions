# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
equivalent -> they share the exact same strcuture and nodes that has the same value
    same structure -> same left, same right (they exist)
    same value -> left.val == left.val, same for right side

"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subNode):
            if not node and subNode:
                return False
            if not subNode and node:
                return False
            if not subNode and not node:
                return True
            if node.val != subNode.val:
                return False
            return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)
        def dfsHelper(node):
            if not node:
                return False
            if dfs(node, subRoot):
                return True
            return dfsHelper(node.left) or dfsHelper(node.right)
        return dfsHelper(root)
            
            
