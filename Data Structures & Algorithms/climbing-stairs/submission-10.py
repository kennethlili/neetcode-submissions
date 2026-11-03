"""
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.


Constraints:

Actions:
    -take1
    -take2
    if n == 0:
        return1
    if n < 0:
        return 0
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0: 
                return 0
            take1 = helper(n -1)
            take2 = helper(n -2)
            memo[n] =  take1 + take2
            return memo[n]
        return helper(n)