class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {} # (src -> (dst, prob))
        for num in (range(n)):
            adj[num] = []
        for i in range(len(edges)):
            (src, dst) = edges[i]
            prob = succProb[i]
            adj[src].append((dst, prob))
            adj[dst].append((src, prob))
        visited = set()
            
     
        maxHeap  = [(-1.0, start_node)] # (prob, dst)

        while maxHeap:
            (nProb, dst)=heapq.heappop(maxHeap)
            visited.add(dst)
            prob = -1 * nProb
            if (dst == end_node):
                return prob
            
            for (ndst, nprob) in adj[dst]:
                if ndst not in visited:
                    curr = nprob * prob
                    heapq.heappush(maxHeap, ((-1 * curr), ndst))
        return 0