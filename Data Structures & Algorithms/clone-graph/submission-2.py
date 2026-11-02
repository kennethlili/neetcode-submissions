"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        valToNode = {}
        if not node:
            return None
        def dfs(node):
            print(node)
            copy = Node(node.val)
            if node.val in valToNode:
                return valToNode[node.val]
            valToNode[node.val] = copy
            for neighNode in node.neighbors:
                copy.neighbors.append(dfs(neighNode))
            return copy
        return dfs(node)

        