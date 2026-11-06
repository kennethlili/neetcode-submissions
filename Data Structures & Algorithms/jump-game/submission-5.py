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
        dp[m - 1] = True
        mrt = m-1

        for i in range(m - 2, -1, -1):
            maxJump = nums[i]
            # endJump = m - i - 1
            # based on the jump we can, we need to find True
            # query True for i <= k
            if  i + nums[i] >= mrt:
                dp[i] = True
                mrt = i

            # for j in range(1, (min(maxJump, endJump)) + 1):
            #     if dp[(i + j)]:
            #         dp[i] = True
            #         break
        print(dp)
        return dp[0]
