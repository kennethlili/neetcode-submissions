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
        for ch, freq in freq.items():
            heapq.heappush(maxheap, (-1 * freq, ch))
        maxFreq = 0
        time = 0
        while maxheap:
            if not maxFreq:
                (nfreq, ch) = heapq.heappop(maxheap)
                freq = nfreq * (-1)
                maxFreq = freq
                time += 1
            else:
                (nfreq, ch) = heapq.heappop(maxheap)
                if (-1 ) * nfreq !=maxFreq:
                    break
                else:
                    time += 1
        length = maxFreq + (maxFreq - 1) * n + (time -1)
        return max(length, len(tasks))
        # while maxheap:
        #     (nfreq, ch) = heapq.heappop(maxheap)
        #     freq = nfreq * (-1)
        #     length = freq + (freq - 1) * n
        #     if not available:
        #         res += length
        #         available = n if freq > 1 else 0
        #         print(res)
        #     else:
        #         inserted = n - available + 1
        #         if inserted + length > res:
        #             res = inserted + length
        #         available -= 1
                
       
        return res
