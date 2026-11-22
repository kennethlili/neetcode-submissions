# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
facts:
    return true if height-balanced, false otherwise
    height-balanced binary tree
        left and right subtree for every node are different by no more than 1
    
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left ,right) + 1
        if dfs(root) == -1:
            return False
        return True