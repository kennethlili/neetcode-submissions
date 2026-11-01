# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Actions:
preorder have the root node: 3
[3,9,20,15,7]
9, 3, 15, 20, 7

rootIndex = 1
len of left: 0:0 -> 1, right len = 2:4 -> 3

left:
index of preorder: 1
index of inorder : 0, 0
9

right:
index of preorder: 2
index of inorder : 2, 4
rootIndex: 3
len of left:  2:2 -> 1, right : 4:4 -> 1

"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        LEN = len(preorder)
        lookup = {}
        for i, n in enumerate(inorder):
            lookup[n] = i

        def helper(preIndex, start, end):
            if start > end:
                return None

            rootVal = preorder[preIndex]
            rootIndex = lookup[rootVal]
            # left, right = None, None
            lefts, lefte = start, rootIndex - 1
            rights, righte = rootIndex + 1, end
            leftLen = lefte - lefts + 1
            left = helper(preIndex + 1, lefts, lefte)
            right = helper(preIndex + 1 + leftLen, rights, righte)
            node = TreeNode(rootVal, left, right)
            return node

        return helper(0, 0, len(inorder) - 1)
