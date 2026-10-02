class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 0
        while(left <= right):
            mid = (left + right) // 2
            t = self.getTotalEatTime(piles, mid)
            print(mid, t,)
            if(t <= h):
                res = mid
                right = mid -1
            else:
                left = mid + 1
        
        return res
    
    def getTotalEatTime(self,piles, e):
        total = 0
        for p in piles:
            total += math.ceil(p/e)
        return total