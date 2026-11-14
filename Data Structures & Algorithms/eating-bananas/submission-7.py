"""
facts:
    arr piles integer, num represent the # of banana in that piles
        - we can only eat that pile of banana in that same hour
        - pils are not sorted in any order

    return the min of k to finihs all the items within h hour

    time: O(max(piles) * n)
    find the k from 1 : max(piles)
    if cannt finihsed, left = mid + 1
    else: right = mid -1
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        while left <= right:
            k = (left + right)//2
            hour = 0
            for n in piles:
                hour += math.ceil(n/k)
            if hour <= h:
                right = k -1
            else:
                left = k + 1
        return left


