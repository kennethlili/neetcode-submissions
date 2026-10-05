class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        while(len(stones) > 1):
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            # if(first == second):
                # destroy both stones
            diff = abs(first-second)
            heapq.heappush_max(stones,diff)
        return stones[0]
