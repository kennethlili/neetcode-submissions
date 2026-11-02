"""
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

Constraints:
nums large, can be negative
calls large
findMedian will also have ans


[1, 3, 2]

2 heap

small,maxHeap:
big,minHeap:

push to small by default
if small[0] > big[0]:
    swap position

check uneven -> their len diff are not greater than 1



"""

class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap
        self.big = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.small and self.big and self.small[0]* (-1) > self.big[0]:
            popN=heapq.heappop(self.small)
            heapq.heappush(self.big, -1 * popN)
        
        if len(self.small) > len(self.big) + 1 :
            popN=heapq.heappop(self.small)
            heapq.heappush(self.big, -1 * popN)

        if len(self.big) > len(self.small) + 1 :
            popN=heapq.heappop(self.big)
            heapq.heappush(self.small, -1 * popN)

    def findMedian(self) -> float:
        if len(self.big) == len(self.small) and self.small and self.big:
            return (self.small[0] * (-1) + self.big[0])/2
        if not self.big or len(self.big) < len(self.small):
            return self.small[0] * -1
        if not self.small or len(self.big) > len(self.small):
            return self.big[0]
        
        