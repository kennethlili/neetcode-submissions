"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        cloned = {}
        cloned[node.val] = Node(node.val)
        while(queue):
            curr = queue.popleft()
            for nd in curr.neighbors:
                if nd.val not in cloned:
                    cloned[nd.val] = Node(nd.val)
                    queue.append(nd)
                cloned[curr.val].neighbors.append(cloned[nd.val])
                         
        return cloned[node.val]