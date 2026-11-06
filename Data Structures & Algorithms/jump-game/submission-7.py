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
        mrt = m - 1
        res = True

        for i in range(m - 2, -1, -1):
            maxJump = nums[i]
            if i + nums[i] >= mrt:
                mrt = i
                res = True
            else:
                res = False
        return res
