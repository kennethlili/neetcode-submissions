"""
Facts:
    return the max area of the container
    area = h (min(heights[i])) * width (index[r] - index[l])
    2 <= height.length <= 100,000

time: O(n^2)
space: O(1)
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        # for i in range(len(heights)-1):
        #     # find the max area after the i pointer
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j -i )
        #         res = max(area,res)
        l, r = 0, len(heights) - 1
        while l < r:
            res = max(min(heights[l], heights[r]) * (r - l), res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
