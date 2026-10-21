class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        cnt = {}
        for n in range(numCourses):
            adj[n] = []
            cnt[n] = 0
        for dst,pre in prerequisites:
            adj[dst].append(pre)
            cnt[pre] += 1
        visited = set()
        res = []
        def dfs(n, cycle):
            if n in cycle:
                return -1
            if n in visited:
                return
            visited.add(n)
            cycle.add(n)
            for nei in adj[n]:
                if dfs(nei, cycle) == -1:
                    return -1
            
            res.append(n)
            cycle.remove(n)
        
        for n in range(numCourses):
            if cnt[n] == 0:
                if dfs(n, set()) == -1:
                    return []
        return res
        


        
