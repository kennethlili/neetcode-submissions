"""
facts:
    arr with integer array
        -not sorted
        - 2 <= arr <= 100,000
        - num can be negative
        - num can be duplicate
    return the arr with the product of all the elements in arr except the element itself
    Each product is guaranteed to fit in a 32-bit integer.
time: O(n^2)
space: O(n)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        surfix = [1] * len(nums)
        prevPrefix = 1
        for j in range(len(nums)-2, -1, -1):
            surfix[j] = surfix[j+1] * nums[j+1]
        for i in range( len(nums)):
            if i ==0:
                currPrefix = 1
            else: 
                currPrefix = prevPrefix * nums[i-1]
            res[i] = currPrefix * surfix[i]
            prevPrefix =    currPrefix 
        
        return res
