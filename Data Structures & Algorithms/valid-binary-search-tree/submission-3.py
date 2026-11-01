# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Actions:
traverse every level
check left < node.val 
check right > node.val
if right or left is False:
    return False
reutrn true by default

have a bound, lower, upper
go left -> curr.val = upper
go right -> curr.val = lower

lower > curr > upper



"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(curr, lower,upper):
            if not curr:
                return True
            if lower >= curr.val or curr.val >= upper:
                return False
            left,right = True,True
            if curr.left:
                left = helper(curr.left, lower, curr.val)
            if curr.right:
                right = helper(curr.right, curr.val, upper)
            return left and right
        INF = float('inf')
        return( helper(root, -1 * INF, INF))





        