class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        cnt = {}
        res = {}

        for n in range(numCourses):
            adj[n] = []
            cnt[n] = 0
            res[n] = set()
        for prereq, lsn in prerequisites:
            adj[prereq].append(lsn)
            cnt[lsn] += 1
        q = deque()
        for n in range(numCourses):
            if cnt[n] == 0:
                q.append(n)
        visited = set()
        while q:
            lsn = q.popleft()
            visited.add(lsn)
            for nei in adj[lsn]:
                copy = res[lsn] | res[nei]
                copy.add(lsn)
                res[nei]= copy
                cnt[nei] -= 1
                if cnt[nei] == 0 :
                    q.append(nei)
        ans = []
        for u,v in queries:
            ans.append(u in res[v])
        return ans