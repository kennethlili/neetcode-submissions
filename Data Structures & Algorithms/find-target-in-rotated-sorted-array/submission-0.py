"""
1. How do we find the sorted k -> rotation

mid pt
mid num greater than r num
- go right -> l = mid + 1

mid num smaller than r 
go left -> r = mid

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getIndex():
            l, r = 0, len(nums) -1
            if len(nums) == 1:
                return 0
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        cutoff = getIndex()
        arr1, arr2 = nums[0: cutoff], nums[cutoff:]
        def bs(arr, offset):
            l, r = 0, len(arr) -1
            while l <= r:
                mid = (l + r) // 2
                n = arr[mid]
                if n == target:
                    return mid + offset
                elif n < target:
                    l = mid +1
                else:
                    r = mid -1
            return -1
        arr = arr1
        offset = 0
        print(arr2)
        if  len(arr2) and arr2[0] <= target <= arr2[-1]:
            arr = arr2
            offset = len(arr1)
        print(arr, offset)
        return bs(arr, offset)
