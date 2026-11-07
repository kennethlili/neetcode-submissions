"""
Facts:
    overlapping => [a,b] [c,d] c<= a <= d or c<= b <= d
    return an array of non-overlapping intervals
    the input is not sorted
    1 <= intervals.length <= 1000
    0 <= start <= end <= 1000
                i
[1,3] [1,4]  [1,5][6,7]

[1,5]
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key =lambda interval: interval[0])
        res = []
        curr = intervals[0]
        print(intervals)
        for i, interval in enumerate(intervals):
            if i == len(intervals) - 1:
                res.append(curr)
                continue
            (currStart, currEnd) = curr
            nxtStart, nxtEnd = intervals[i+1]
            if currStart<= nxtStart <= currEnd or currStart<= nxtEnd <= currEnd:
                curr = [min(currStart,nxtStart ), max(currEnd, nxtEnd )]
            else:
                res.append(curr)
                curr = intervals[i+1]

        return res