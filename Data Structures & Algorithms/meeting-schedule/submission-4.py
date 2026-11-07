"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Facts:
    interval must be (start, end) format
    conflict  = [starta, enda] [startb, endb] startb< enda
    the arr is not sorted
    determine there is any conflict
    arr can be empty

"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if not intervals:
        #     return True
        # intervals.sort(key=lambda x: x.start)
        # prevEnd = intervals[0].end
        # for i in range(1, len(intervals), 1):
        #     currStart = intervals[i].start
        #     if currStart < prevEnd:
        #         return False
        #     prevEnd = intervals[i].end
        # return True
        m = len(intervals)
        for i in range(m):
            prev = intervals[i]
            for j in range(i+1, (m), 1):
                curr = intervals[j]
                if not(curr.start >= prev.end or curr.end <= prev.start):
                    return False
                
        
        return True


