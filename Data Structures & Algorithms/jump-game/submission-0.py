"""
Facts:
    We can move kth index when we reach nums[i] = k
    We can move to anywhere less than the k
    k can be zero, which lead to no more moving
    1<=len(nums)<= 1000
    return True if can reach the last index
        [0] is also true
    return False if not
    index = 1, len = 3
    [1000, 1000, 1]

time: O(n^2)

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        memo = {}
        def canReachLast(i):
            if i in memo:
                return memo[i]
            if i == m -1:
                return True
            maxJump = nums[i]
            if maxJump == 0:
                return False
            endJump = m - i - 1
            ran = maxJump
            if maxJump > endJump:
                ran = endJump
            for j in range(1, (ran) + 1):
                if canReachLast(i + j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return canReachLast(0)