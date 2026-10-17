class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        captialHeap = []  # min heap
        for i in range(len(capital)):
            heapq.heappush(captialHeap, (capital[i], profits[i]))
        profitHeap = []  # max heap

        for _ in range(k):
            while len(captialHeap) and (captialHeap[0][0] <= w):
                (cap, pro) = heapq.heappop(captialHeap)
                heapq.heappush(profitHeap, -1 * pro)

            if not profitHeap:
                break
            w = w + (-1 * heapq.heappop(profitHeap))

        return w
