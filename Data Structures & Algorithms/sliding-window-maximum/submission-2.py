"""
facts:
    nums, arr of integer and a k -> slidig window size
    return a list that contains the max element within the k window
    at each step we slide one position to rhe right
    until the len(nums) - k
    7, until index4 = len - k
    time: o(n)
    space: O(n)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # for i in range(0, len(nums) - k + 1):
        #     temp_max  = float('-inf')
        #     for j in range(i, i + k):
        #         temp_max = max(temp_max, nums[j])
        #     res.append(temp_max)
        # return res
        currMap = {}
        currMax = float('-inf')
        left = 0
        for r, num in enumerate(nums):
            if num not in currMap:
                currMap[num] = 0
            currMap[num] += 1
            currMax = max(currMax, num)
            if r - left + 1 > k:
                currMap[nums[left]] -= 1
                

                if currMap[nums[left]] == 0:
                    del currMap[nums[left]]
                if currMax == nums[left] and nums[left] not in currMap:
                    currMax = max(currMap)
                left += 1
            if r-left + 1 == k:
                res.append(max(currMap))
        return res



