'''
O(logn)
Binary Search

res = nums[0]

mid
if mid > l
go right -> l = mid + 1

mid <= l
go left -> r = mid - 1

update our res, min on every action

handle len == 2 case
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while( l <= r):
            ln = r -l + 1
            if ln == 2:
                res = min(res , nums[r], nums[l])
                break

            mid = (r+ l) //2
            n = nums[mid]

            res = min (res, n)
            if n > nums[l]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                r = mid -1
            
        return res

        
