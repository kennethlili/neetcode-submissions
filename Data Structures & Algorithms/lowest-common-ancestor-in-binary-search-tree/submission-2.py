# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BST: all node val are unique
    mean smaller val left, bigger val right
return the LCA of the p and q
    LCA -> contain both p and q and it is the lowest
        both p and q are descendants
            The ancestor is allowed to be a descendant of itself.
        could be the root that p /q or root that upper than it once
    
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        def dfs(root):
            if not root: return
            if p.val <= root.val <= q.val: 
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            return left or right
        return dfs(root)