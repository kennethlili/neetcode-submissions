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

"""
Bounds: n: [0,n]
n decresing-> 
n small ++ big
"""
class Solution:
    def climbStairs(self, n: int) -> int:
          
           
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            
            if i < 0: 
                dp[i] =  0
                continue
            dp[i] =  dp[i - 1] + dp[i -2]
        return dp[n]