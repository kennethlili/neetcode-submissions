class Solution:
    def trap(self, height: List[int]) -> int:
        # get max value from the left
        # leftarr = []
        leftmax = 0

        rightarr = [0] * len(height)
        rightmax = 0
        

        res = 0

        for r in range(len(height) - 1, -1 ,-1):
            rightarr[r] = (rightmax)
            rightmax = max(rightmax, height[r])

        
        for i,h in enumerate(height):
            templeftmax = leftmax
            # leftarr.append(leftmax)
            leftmax = max(leftmax, height[i])
            
            minLR = min(templeftmax, rightarr[i])
            watertrapped = max(minLR - h, 0)
            res += watertrapped
        return res