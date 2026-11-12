"""
facts:
    price integer arr
        not sorted
    we can buy in any days
    but only sell after the buy day
    we can also not make any actions -> profit = 0
    profit = sell price - buy price
    arr, 1 <= prices.length <= 100
    price 0 <= prices[i] <= 100

time: O(n^2)
space: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i,buy in enumerate(prices):
            for j in range(i+1, len(prices)):
                prof = prices[j] - buy
                res = max(prof, res)
        return res