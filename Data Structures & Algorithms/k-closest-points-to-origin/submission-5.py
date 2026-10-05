class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pt in points: 
            x,y = pt
            distance = x**2+ y**2
            heap.append([distance, x,y])
        heapq.heapify(heap)
        res = []
        for i in range(k):
            _,x,y=heapq.heappop(heap)
            res.append([x,y])
        return res

        
