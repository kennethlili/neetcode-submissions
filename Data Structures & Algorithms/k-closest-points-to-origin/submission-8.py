"""
return the k closest point to the origin
    in any order
k -> 1th index
distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))

nlogn -> nlogk
n -> k
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i, (x, y) in enumerate(points):
            heapq.heappush_max(maxHeap, (x**2 + y**2, i))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        return [points[pt[1]] for pt in maxHeap]
