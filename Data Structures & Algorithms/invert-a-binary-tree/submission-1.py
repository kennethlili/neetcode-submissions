# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return
            tmpL, tmpR = node.left, node.right
            node.left = helper(tmpR)
            node.right = helper(tmpL)
            return node
        return helper(root)
        
