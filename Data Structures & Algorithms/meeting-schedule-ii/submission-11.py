"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Actions:
    we need to know what meeting room is now occupied


"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        intervals.sort(key=lambda x: x.start)
        res = 0
        for iv in intervals:
            if not minHeap:
                minHeap.append(iv.end)
            else:
                if iv.start<minHeap[0]:
                    heapq.heappush(minHeap, iv.end)

                else:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, iv.end)
        
        return len(minHeap)
