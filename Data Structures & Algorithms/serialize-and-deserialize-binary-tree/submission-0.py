# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
[1,2,3,null,null,4,5]
"&"

res = "10,2,3,N,N,4,5"
BFS:
1
2
need to insert null,( if q has vale)
3
null, null, 4,5,


for char in data:

10
left = 2
right = 3


"""
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        SUR = ","
        NULL = 'N'
        res = ""
        while q:
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                if not node:
                    res += (NULL + SUR)
                else:
                    tmp = str(node.val) + SUR
                    res += tmp
                    q.append(node.left)
                    q.append(node.right)
        return res
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        SUR = ","
        NULL = 'N'
        temp = ""
        arr = []
        for ch in data:
            if ch == SUR:
                if temp == None:
                    arr.append(None)
                elif temp:
                    arr.append(int(temp))
                temp = ""
            elif ch == NULL:
                temp = None
            else:
                temp += ch
        if not arr[0]:
            return None
        root = TreeNode(arr[0])
        q = deque()
        q.append(root)
        index = 1
        while q:
            node = q.popleft()
            if arr[index]:
                node.left = TreeNode(arr[index])
                q.append(node.left)
            index += 1
            if arr[index]:
                node.right = TreeNode(arr[index])
                q.append(node.right)
            index += 1
        
        return root
                

                

        











