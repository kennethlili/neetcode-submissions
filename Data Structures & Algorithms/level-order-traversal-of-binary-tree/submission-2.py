# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if(root):
            q.append(root)
        while(len(q) > 0):
            tempLen = (len(q))
            tempArr = []
            for i in range(len(q)):
                curr = q.popleft()
                if(curr.left):
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                tempArr.append(curr.val)

                if(i == tempLen - 1):
                    res.append(tempArr)
                    tempArr=[]
            
        return res