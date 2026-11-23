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
        # if max(q.val, p.val) < root.val :
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if min(q.val,p.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # return root
        while(root):
            if max(q.val, p.val) < root.val :
                root = root.left
                continue
            if min(q.val,p.val) > root.val:
                root = root.right
                continue
            return root