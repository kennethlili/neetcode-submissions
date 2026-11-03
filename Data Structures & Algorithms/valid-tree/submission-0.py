class UnionFind:
    def __init__(self,n) -> None:
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    def find(self,n):
        if n == self.parent[n]:
            return self.parent[n]
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    def union(self,n1, n2):
        p1, p2 = self.find(n1) , self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2]>self.rank[p1] :
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        uf = UnionFind(n)
        for a,b in edges:
            if not uf.union(a,b):
                return False
        return True


