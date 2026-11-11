"""
Facts:
    return the max area of the container
    area = h (min(heights[i])) * width (index[r] - index[l])
    2 <= height.length <= 100,000

time: O(n^2) -> O(n)
space: O(1)
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            res = max(min(heights[l], heights[r]) * (r - l), res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
