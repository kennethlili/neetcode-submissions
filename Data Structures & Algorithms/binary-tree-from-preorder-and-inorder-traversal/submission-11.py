# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
preorder gives us the rootval
inorder gives us the len of the left and right
I am looking at a subtree where its root are given by
preorder[pre_start:pre_end]
-> root preorder[pre_start] = rootVal
-> inidx = inorder.index(rootVal)
left_inorder_s = start, inidx - 1 -> len = end - start + 1
right_inorder_e = inidx + 1, end -> len = end - start + 1
left_preorder = pre_s + 1
right_preorder = pre_s + 1 + len(left)

"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {}
        for i, n in enumerate(inorder):
            lookup[n] = i
        def helper(preorderIdx, start, end):
            if start > end:
                return None
            val = preorder[preorderIdx]
            inIdx = lookup[val]
            lenL = inIdx - start
            lenR = end - inIdx
            node = TreeNode(val)
            node.left = helper(preorderIdx + 1, start, inIdx- 1)
            node.right = helper(preorderIdx + lenL + 1, inIdx + 1, end)
            return node

        return helper(0, 0, len(inorder) -1 )
