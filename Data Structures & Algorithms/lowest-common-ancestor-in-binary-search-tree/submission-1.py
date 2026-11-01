# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
conditions:

if p and q is p < curr < q, or vice versa
return curr

if p == curr, q> curr / <,
return curr

curr > p and > q
go left

curr < p and < q
go right

"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(curr):
            if curr.val > p.val and curr.val > q.val:
                return helper(curr.left)
            if curr.val < p.val and curr.val < q.val:
                return helper(curr.right)
            else:
                return curr
        return helper(root)
        
        
