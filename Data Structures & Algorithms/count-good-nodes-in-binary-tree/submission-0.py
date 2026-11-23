# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
good node -> the path to the node contains no node with a val > node x
    root is the good node
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def isGoodNode(val,path):
            for n in path:
                if n>val:
                    return False
            return True
        def dfs(node, currVal):
            if not node:
                return
            # if isGoodNode(node.val, path):
            #     res[0] += 1
            if currVal <= node.val:
                res[0] += 1 
            
            left = dfs(node.left,max(currVal, node.val) )
            right = dfs(node.right,max(currVal, node.val) )
            return
        dfs(root, root.val)
        return res[0]

