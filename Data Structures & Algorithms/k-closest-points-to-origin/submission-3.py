class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSort(points, 0, len(points) - 1)
        return points[:k]

    def quickSort(self, points, left, right):
        if left < right:
            p = self.partition(points, left, right)
            self.quickSort(points, left, p - 1)
            self.quickSort(points, p + 1, right)

    def partition(self, points, left, right):
        p = right
        pVal = self.getDistance(points[p])
        i, j = left, left
        while j < p:
            if self.getDistance(points[j]) < pVal:
                points[i], points[j] = points[j], points[i]
                i += 1
            j += 1

        points[p], points[i] = points[i], points[p]
        return i

    def getDistance(self, point):
        x, y = point
        return (x) ** 2 + y**2
