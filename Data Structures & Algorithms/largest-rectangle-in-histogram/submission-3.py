"""
facts:
    arr of heights -> represent the height of a bar
    the width of each bar is 1
    return the area of the largest rectangle that can be formed among the bars
    area of the Rectangle = width x height
    we got to control the height instead of the width
    we need to find the max height
    [7,1]
    min(picked h) * len(picked element)

    when we include the min value in the array, the max size will only be including the entire arr
    
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
     
        heights = heights + [0]
        stack = []
        for i, h in enumerate(heights):
            while stack and h < stack[-1][0]:
                popVal=stack.pop()
                left = stack[-1][1] if stack else -1
                right = i
                width = right - left - 1
                # width = i - stack[-1][1] -1 if stack else 1
                area = width * popVal[0]
                res = max(area,res)

            
            stack.append((h,i))
        
        return res
                
            
