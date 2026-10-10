class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = {}
        for (pre, next) in prerequisites:
            if pre not in coursemap:
                coursemap[pre] = []
            if next not in coursemap:
                coursemap[next] = []
            coursemap[pre].append(next)
        print(coursemap)
        def dfs(curr, visiting):
            if curr in visiting: return False
            if coursemap[curr] == []: return True
            visiting.add(curr)
            for co in coursemap[curr]:
                if not dfs(co, visiting): return False
            visiting.remove(curr)
            coursemap[curr] = []
            return True
        
        for key, val in coursemap.items():
            if not dfs(key,set()): return False
        return True

