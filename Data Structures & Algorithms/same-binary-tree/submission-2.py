# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            if not t2 or not t1:
                return False
            if t1.val != t2.val:
                return False
            if not (dfs(t1.left, t2.left) and dfs(t1.right, t2.right)):
                return False
            return True
        return dfs(q, p)
           
