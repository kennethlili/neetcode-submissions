"""
Facts:
    overlapping => [a,b] [c,d] c<= a <= d or c<= b <= d
    return an array of non-overlapping intervals
    the input is not sorted
    1 <= intervals.length <= 1000
    0 <= start <= end <= 1000

why do we need the sort?
we wnat to compare to the next value to merge
why do we need the next value?
so that we wont missed 

[1,3]   [1,5] [6,7] 

[1,5]
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for (start, end) in intervals:
            if res and start <= res[-1][1]:
                res[-1] = [res[-1][0], max(end, res[-1][1])]
            else:
                res.append([start,end])
        return res
