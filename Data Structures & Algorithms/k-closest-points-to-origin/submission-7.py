"""
return the k closest point to the origin
    in any order
k -> 1th index
distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))


"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i, (x, y) in enumerate(points):
            dist = x**2 + y**2
            heapq.heappush_max(maxHeap, (dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        # points.sort(key=lambda point: point[0]**2 + point[1]**2)
        # res = []
        # for i in range(k):
        #     res.append([points[i][1], points[i][2]])
        # return res
        return [[item[1], item[2]] for item in maxHeap]
