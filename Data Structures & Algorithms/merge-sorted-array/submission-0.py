class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - 1
        i = len(nums1) - n - 1
        j = len(nums2) - 1
        while (k >= 0):
            print(i,j)
            if(i < 0):
                nums1[k] = nums2[j]
                j -= 1
            elif (j < 0):
                nums1[k] = nums1[i]
                i -=1
            else:
                if(nums1[i] >= nums2[j]):
                    print(k, 'left')
                    nums1[k] = nums1[i]
                    i -= 1
                else: 
                    print(k, 'right')
                    nums1[k] = nums2[j]
                    j -= 1
            k -= 1
        