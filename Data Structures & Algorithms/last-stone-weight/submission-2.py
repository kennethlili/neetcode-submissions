'''

'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone_1 = heapq.heappop_max(stones)
            stone_2 = heapq.heappop_max(stones)
            new_stone = abs(stone_1 - stone_2)
            if new_stone != 0:
                heapq.heappush_max(stones,new_stone)
        if not stones:return 0
        return stones[0]