"""
facts:
    return the all the 3 numbers that add up to 0, ordering doesnt matter
        - not guartane to have the result
        - we cannot reuse the same index again
        - combination do matter -> [-1,-1,2] = [-1, 2, -1], it has be distinct
    arr are not guartane to be sorted
    3 <= arr <= 3000
    num can be negative
problem:
    how do we have all the triplets that add up to zero?
        loop 3 times
    how do we differate the distinct triplets?
        sorting it will differate the distinct result
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
           
            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1

        ans = []
        # for tmp in res:
        #     (t1, t2, t3) = tmp
        #     ans.append([t1, t2, t3])
        return list(res)
