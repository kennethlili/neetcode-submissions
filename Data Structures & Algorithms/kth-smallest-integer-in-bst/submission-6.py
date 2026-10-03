# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = [0,0]
        self.dfs(root,k, i)
        return i[1]
    def dfs(self,root,k, i):
        if(not root):
            return
        if self.dfs(root.left,k,i):
            return True
        i[0] += 1
        if(i[0] == k):
            i[1] = root.val
            return True
        if self.dfs(root.right,k,i):
            return True