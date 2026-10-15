class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}
        for i in range(1, (len(edges)) + 1, 1):
            par[i] = i
            rank[i] = 0
        def find(n):
            p = par[n]
            while par[p] != p:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1

            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True
        
        for (i,j) in edges:
            if not union(i,j):
                return [i,j]

