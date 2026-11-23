# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BST:
    all value are unique
    every val in the left is < the node
    every val in the right is > the node

"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        newK = [k]

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            if left != -1:
                return left
            newK[0] -= 1
            if newK[0] == 0:
                return node.val
            return dfs(node.right)

        return dfs(root)
