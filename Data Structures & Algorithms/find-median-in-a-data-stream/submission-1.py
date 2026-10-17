class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if len(self.small) and len(self.large) and (self.small[0] * -1 )> self.large[0]:
            val = - 1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = - 1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if not len(self.small) and not len(self.large):
            return 0
        if(len(self.small) > len(self.large)):
            return (self.small[0] * -1 )
        if(len(self.small) < len(self.large)):
            return self.large[0]
        return ((self.small[0] * -1 ) + self.large[0])/2
        