"""
Facts:
    intervals is sorted by start
    intervals also non-overlapping
    start < end
    overlapping = [starta, enda] , [enda, endb] or vice versa -> any end <= any start/ vice-verse
    insert newInterval into intervals which intervals has no overlapping and maintain the sorted property
    interval always len 2
    interval time 0 <= 100000, non-negative
    0 <= intervals.length <= 10000
    do we need to return interval in place?

Brute Force:
    1. insert the new interval by comparing the start to maintain the sorted order O(n)
    2. check on each interval to see any overlapping O(n^2)
[[1,3],[2,5],[4,6]]
1,5, [4,6]

Bound:
i: [0, m -1]

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        m = len(intervals)
        insertIndex = 0
        for i in range(m):
            if intervals[i][0] < newInterval[0]:
                insertIndex = i + 1
        intervals.insert(insertIndex, newInterval)
        newRes = []

        def mergeIntervals(i, curr):
            if i == len(intervals) - 1:
                newRes.append(curr)
                return
            nxtStart, nxtEnd = intervals[i + 1]
            currStart, currEnd = curr
            if (currStart <= nxtStart and nxtStart <= currEnd) or (
                currStart <= nxtEnd and nxtEnd <= currEnd
            ):
                return mergeIntervals(
                    i + 1,
                    [min(currStart, nxtStart), max(currEnd, nxtEnd)],
                )
            newRes.append(curr)
            return mergeIntervals(i + 1, intervals[i + 1])
        curr = intervals[0]
        for i in range(len(intervals)):
            if i == len(intervals) - 1:
                newRes.append(curr)
                break
            nxtStart, nxtEnd = intervals[i + 1]
            currStart, currEnd = curr
            if (currStart <= nxtStart and nxtStart <= currEnd) or (
                currStart <= nxtEnd and nxtEnd <= currEnd
            ):
                curr = [min(currStart, nxtStart), max(currEnd, nxtEnd)]
                # continue
            else:
                newRes.append(curr)
                curr = intervals[i + 1]

        # mergeIntervals(0, intervals[0])
        return newRes
