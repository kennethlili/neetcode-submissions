class UF:
    def __init__(self, length):
        par = {}
        rank = {}
        for n in range(length):
            par[n] = n
            rank[n] = 0
        self.par = par
        self.rank = rank
    def find(self,n):
        if self.par[n] == n:
            return self.par[n]
        self.par[n]= self.find(self.par[n])
        return self.par[n]
    def union(self,n1, n2):
        p1, p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        res = n

        for (n1, n2) in edges:
            if uf.union(n1,n2):
                res -= 1
        
        return res