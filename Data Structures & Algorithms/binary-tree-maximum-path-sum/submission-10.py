# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
facts:
    path sum is the sum of the node val in the path
    path:
        node cannot appear more than once
        doesnt need to included the root
    actions:
        take the root, left and right ->cant bring forward
        take either left and right
        take the root only

"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(node):
            if not node:
                return 0
            maxL = max(0, dfs(node.left))
            maxR = max(0, dfs(node.right))
            tempVal = node.val + max(maxL, maxR)
            bend = node.val + maxL + maxR
            res[0] = max(res[0], max(bend, tempVal))
            return tempVal

        dfs(root)
        return res[0]
