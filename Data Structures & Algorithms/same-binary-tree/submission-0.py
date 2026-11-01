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
                return -1
            if t1 and not t2:
                print('not')
                return False
            if t2 and not t1:
                print('not')
                return False
            if t1.val != t2.val:
                print('not')
                return False
            if  dfs(t1.left, t2.left) == False:
                print('left')
                return False
            if  dfs(t1.right, t2.right)== False:
                print('right')
                return False
        print('-1', dfs(q,p))
        if  dfs(q,p) == False:
            return False
        return True

