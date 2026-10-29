'''
You may choose to not make any transactions, in which case the profit would be 0

Observations:
we want buy as L as po
we want to sell as H as po

profit = prices[r]  - prices[l]

actions:
s - b < 0 
move b to s

r - l >= 0
move s+= 1


'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0, 1
        if (len(prices) <= 1):
            return 0
        res = 0
        while (s < len(prices)):
            prof = prices[s]  - prices[b]
            if prof < 0:
                b = s
            else:
                s += 1
            res = max(res,prof)
        return res
