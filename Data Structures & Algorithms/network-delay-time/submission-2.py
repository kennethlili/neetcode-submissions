class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        # path = {k: 0}
        path = {}
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        res = 0
        for i in range(1, n+1,1):
            adjList[i] = []
        for (src, dst, time) in times:
            adjList[src].append((dst, time))
        while(len(minHeap) > 0 and len(path) < n):
            (cCost, cDst) = heapq.heappop(minHeap)
            if cDst  in path:
                continue
            path[cDst] = cCost
            res = max(res, cCost)
            neighbours=adjList[cDst]
            for (dst,cost) in neighbours:
                heapq.heappush(minHeap,(cost + path[cDst],dst))

        print(path)
        
        if len(path) < n:
            return -1
        
        return res
