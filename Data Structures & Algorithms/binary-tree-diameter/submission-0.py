# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
diameter -> len of the longest path between any two node within the tree
    does have to pass thru the root
len of 2 nodes is the number of edges between the nodes in one time

return the diameter

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node):
            if  (not node.left and not node.right):
                return 0
            left = 0
            right = 0
            if node.left:
                left = 1 + dfs(node.left)
            if node.right:
                right = 1 + dfs(node.right)
            res[0] = max(res[0], left+ right)
            return max(left,right)
        dfs(root)
        return res[0]