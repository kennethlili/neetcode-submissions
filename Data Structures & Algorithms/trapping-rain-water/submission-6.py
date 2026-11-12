"""
facts:
    height arr non negative integer
        num represent the height, with width 1
    return the total amt of water can be Trapped
    find the gap between the area


O(n^2)

we want to track the leftMax and rightMax without an arr
-> pointer to store the leftMax and rightMax on our way to middle
-> min of leftMax and rightMax

l < r:
    area = leftMax - height i
    l += 1
    update leftMax
else:
    area = rightMax - height i
    r -= 1
    updateRightMaz
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # def getRightMax():
        #     rightMaxArr = [0]* (len(height))
        #     currMax = 0
        #     for i in range(len(height) -1, -1, -1):
        #         rightMaxArr[i] = currMax
        #         currMax = max(currMax, height[i])
        #     return rightMaxArr
        # res = 0
        # rightMaxArr = getRightMax()
        # currMax = 0

        # for i, h in enumerate(height):
        #     rightMax = rightMaxArr[i]
        #     areaAtI = min(currMax, rightMax) - h
        #     res += max(areaAtI, 0)
        #     currMax = max(h, currMax)
        # return res
        res = 0
        l, r = 0, len(height) - 1
        leftMax,rightMax = 0 , 0
        while l< r:
            if height[l] < height[r]:
                areaAtI = max(0, leftMax - height[l])
                res += areaAtI
                leftMax = max(leftMax, height[l])
                l+= 1
            else:
                areaAtI = max(0, rightMax - height[r])
                res += areaAtI
                rightMax = max(rightMax, height[r])
                r-= 1
        return res

