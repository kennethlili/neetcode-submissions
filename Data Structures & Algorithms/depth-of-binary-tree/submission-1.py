# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
depth = farthest leaf node including the root -> level
depth first search


"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if not root:
            return 0
        queue.append(root)
        level = 0
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        return level