# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
check root val == subroot val
true- > 

"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            left = dfs(root.left, subRoot.left)
            right = dfs(root.right, subRoot.right)
            return left and right
        def dfsHelper(root,subroot):
            if not root:
                return

            rt = dfs(root,subroot)
            if rt:
                return rt
            else:
                return dfsHelper(root.left, subroot) or dfsHelper(root.right, subroot)
        
        return dfsHelper(root,subRoot) == True
