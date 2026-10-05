class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for pt in points:
            x,y = pt
            distance = x**2+ y**2
            heapq.heappush(maxHeap,[distance, x,y])
        res = []
        for i in range(k):
            _,x,y=heapq.heappop(maxHeap)
            res.append([x,y])
        return res

        
