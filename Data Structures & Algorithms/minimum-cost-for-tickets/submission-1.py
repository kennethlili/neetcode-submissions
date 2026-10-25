"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
- interger from 1-365
-days are increasing order
- cost is med in size

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,

a 7-day pass is sold for costs[1] dollars, and

a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a *7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

find the minimum cost to cover all the nums in days


Actions:
take 1, 7, 30 days pass
move the day pter to correct days ->day 1 take 1 days pass, 1 + 1 -> y, move the pter when day val < y
take all days pass

"""


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayPassMap = {0: 1, 1: 7, 2: 30}
        memo = {}

        def getPter(i, dayType):
            ni = i
            while ni < len(days) and days[ni] < days[i] + dayPassMap[dayType]:
                ni += 1
            return ni

        def dfs(i):
            if i >= len(days):
                return 0 
            if i in memo:
                return memo[i]
            take1 = costs[0] + dfs(getPter(i, 0))
            take7 = costs[1] + dfs(getPter(i, 1))
            take30 = costs[2] + dfs(getPter(i, 2))
            best = min(take1, take7, take30)
            memo[i] = best
            return memo[i]
        return dfs(0)
