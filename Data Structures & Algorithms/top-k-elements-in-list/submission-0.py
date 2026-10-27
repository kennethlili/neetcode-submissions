'''
Actions:
iterate the nums.
hashmap ={
    1:1
    2:2
    3:3
}

maxheap (cntVal, num)
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        maxheap = []
        for num, count in cnt.items():
            maxheap.append((-1 * count, num))
        heapq.heapify(maxheap)
        res = []
        for _ in range(k):
            (_, num) = heapq.heappop(maxheap)
            res.append(num)
        return res