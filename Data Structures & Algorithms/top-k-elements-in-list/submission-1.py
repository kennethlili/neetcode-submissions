'''
nums huge
n medium
    -negative number, cannot use it for arr index


cnt = {
1:1
2:2
3:3
}

maxheap
turn the cnt into maxheap
for each k, heappop

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        maxheap = [] ## (freq, n)
        for n, freq in cnt.items():
            heapq.heappush(maxheap, (-1 * freq, n))
        res = []
        for _ in range(k):
            (_, n) = heapq.heappop(maxheap)
            res.append(n)
        
        return res
            