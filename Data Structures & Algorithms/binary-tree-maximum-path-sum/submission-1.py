# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
root = [-15,10,20,null,null,15,5,-5]
Actions:
in order
change yhe val to max in place

get the max of each node:
10

at -5, max(0, -5)
at 15, 15 + 0 -> 15
at 5, 5
at 



"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1 * float('inf')
        def dfs(curr):
            nonlocal res
            if not curr:
                return

            dfs(curr.left)
            dfs(curr.right)
            left, right = 0,0
            if curr.left:
                left = max(left, curr.left.val)
            if curr.right:
                right = max(right, curr.right.val)
            currval = max(left,right) + curr.val

            res = max(res, currval,curr.val + left + right)
            curr.val = max(0, currval)
        dfs(root)
        return res
        