"""
return the k closest point to the origin
    in any order
k -> 1th index
distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))


"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        res = []
        for i in range(k):
            res.append(points[i])
        return res
