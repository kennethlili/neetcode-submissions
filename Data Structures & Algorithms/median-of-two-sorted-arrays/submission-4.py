"""
facts:
    nums1 with size m and nums2 with size n
    nums1 and nums2 are sorted in ascending order
    return the median value among all element of two arrays
    O(log(m+n)) in time
    
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_len = m + n
        left_len = math.ceil(total_len / 2)
        right_len = total_len- left_len
        left, right = 0 , m
        left_part, right_part = 0,0
        while left <= right:
            mid = (left + right ) //2
            max_1 = float('-inf') if mid == 0 else nums1[mid - 1]
            min_1 = float('inf') if mid >= m else nums1[mid]
            len_2 = left_len - mid
            print(mid, len_2)
            max_2 = float('-inf')if len_2 == 0 else nums2[len_2 - 1]
           
            min_2 = float('inf') if len_2 >= n else nums2[len_2]
            # if max(max_1, max_2) > min(min_1, min_2):
            #     left = mid + 1
            if max_1 > min_2:
                right = mid -1
            elif max_2 > min_1:
                left = mid + 1
            else:
                if left_len == right_len:
                    return (max(max_1, max_2)  + min(min_1, min_2) ) /2
                else:
                    return (max(max_1, max_2))
        

        