class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for pre, dst in prerequisites:
            adj[pre].append(dst)
            indegree[dst] += 1
        premap = [set() for _ in range(numCourses)]
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        while q:
            lsn = q.popleft()
            for n in adj[lsn]:
                copy = premap[n] | premap[lsn]
                copy.add(lsn)
                premap[n] = copy
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        print(premap)
        return [u in premap[v] for u, v in queries]
