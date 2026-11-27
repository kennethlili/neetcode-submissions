"""
tasks[i] A-Z
each run a single task only, and we can take all order of the task
identical tasks must be seperate by at least n CPU cycle

return the min number of cycles to complete all tasks

we want to start with identical tasks when availble

A->B->C-> ->A->B-> -> -> A
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        available = 0
        freq = {}
        for t in tasks:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1
        output = []
        maxheap = []
        for fq in freq.values():
            heapq.heappush(maxheap, (-1 * fq))
        maxFreq = 0
        time = 0
        while maxheap:
            if not maxFreq:
                maxFreq = heapq.heappop(maxheap) * (-1)
            else:
                if (-1) * heapq.heappop(maxheap) != maxFreq:
                    break
            time += 1
        length = maxFreq + (maxFreq - 1) * n + (time - 1)
        return max(length, len(tasks))
