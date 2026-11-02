"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
[course, prerequisites]

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.

find is it possible to finished all the courses

Constraints:
numCourses med
prerequisites med
only have one prerequisites

finding the cycle
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, preq in prerequisites:
            adj[preq].append(course)
        visited = set()
        safe = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crs in safe:
                return True
            if not adj[crs]:
                return True
            visited.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            safe.add(crs)
            return True
        for i in range(numCourses):
            # print(dfs(i),i)
            res = dfs(i)
            if res == False:
                return False
        
        return True



