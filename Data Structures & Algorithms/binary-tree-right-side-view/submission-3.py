# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if(root):
            q.append(root)
        while((len(q) > 0)):
            arr = []
            l = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
                arr.append(curr.val)
                if(i == l -1):
                    res.append(arr)
                    arr = []

        result = []
        for ar in res:
            result.append(ar[-1])
        return result
                    

