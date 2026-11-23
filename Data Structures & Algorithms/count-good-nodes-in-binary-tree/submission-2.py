# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
good node -> the path to the node contains no node with a val > node x
    root is the good node
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # res = [0]

        def dfs(node, currVal):
            if not node:
                return 0
            res = 0
            if currVal <= node.val:
                res += 1
            maxVal = max(currVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
        # return res[0]
