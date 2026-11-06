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

time: O(2^n)
Bound:
i: [0, len(nums) - 1]

ordering:
i: big before small

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        dp = [False] * m
       
        for i in range(m -1 , -1, -1):
            if i == m -1:
                dp[i] =  True
                continue
            maxJump = nums[i]
           
            endJump = m - i - 1
            ran = maxJump
            if maxJump > endJump:
                ran = endJump
            for j in range(1, (ran) + 1):
                if dp[(i + j)]:
                    dp[i] =  True
                    break
        print(dp)
        return dp[0]