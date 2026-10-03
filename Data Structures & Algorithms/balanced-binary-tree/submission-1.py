# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # res = [True]
        # self.height(root, res)
        # return res[0]
        try:
            self.height(root,[True])
            return True
        except ValueError:
            return False
    def height(self,root,res):
        if not root:
            return 0
        left, right = self.height(root.left,res), self.height(root.right,res)
        if abs(left-right) > 1:
            raise ValueError('unbalanced')
            # res[0] = False
            # return 0
        h =  1 + max(left,right)
        print(root.val, h)
        return h