class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, cache):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if(n in cache): return cache[n]
            cache[n] = dp(n-1,cache) + dp(n-2,cache)

            return cache[n]
        return dp(n, {})        