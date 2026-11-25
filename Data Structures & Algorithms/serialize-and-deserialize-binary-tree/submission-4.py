# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
transform a binary tree -> string
recover the binary tree from the string

"1,2,3,N,N,4,5"
[1,2,3,None,None,4,5]
[1]
node(1)
[node(1)]
node.left = node(2)
node.right = node(3)
[2,3]
"""


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        arr = []
        while queue:
            node = queue.popleft()
            if not node:
                arr.append("N")
            else:
                arr.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(arr)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        arr = data.split(",")
        root = TreeNode(arr[0])
        queue = deque([root])
        idx = 1
        while queue:
            if idx >= len(arr):
                break
            node = queue.popleft()
            if not node:
                continue
            node.left = TreeNode(int(arr[idx])) if arr[idx] != "N" else None
            idx += 1
            queue.append(node.left)
            node.right = TreeNode(int(arr[idx])) if arr[idx] != "N" else None
            idx += 1
            queue.append(node.right)

        return root
