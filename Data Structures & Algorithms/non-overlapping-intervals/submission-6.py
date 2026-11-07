"""
Facts:
    interval always [start, end]
    overlapping => [start_a,end_a] [start_b,end_b] -> start_b<end_a
    find the min number of interval to remove so that the arr is non-overlapping
    1 <= arr <= 100,000
    interval value can be negative
    arr is not guartne to be sorted

Question:
    how do we know the arr is non-overlapping?
        -loop the arr and check every element [start_a,end_a] [start_b,end_b] -> start_b<end_a


"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0] ))
        prevEnd = float("-inf")
        res = 0
        for i in range(len(intervals)):
            currStart, currEnd= intervals[i]
            # overalpping
            if currStart<prevEnd:
                res += 1
                continue
            prevEnd = currEnd


        return res

