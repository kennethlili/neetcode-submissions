# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) > 1:
            midPoint = len(pairs)//2
            left = pairs[:midPoint]
            right = pairs[midPoint:]


            self.mergeSort(left)
            self.mergeSort(right)

            self.merge(pairs, left, right)
        return pairs

    def merge(self,arr, left, right):
        # left arr
        l = 0
        # right arr
        r = 0
        # arr 
        k = 0
        leftKeys = self.getKeys(left)
        rightKeys = self.getKeys(right)


        while (l<len(left) and r<len(right)):
            lVal,rVal = leftKeys[l] , rightKeys[r]
            if(lVal <= rVal):
                arr[k] =left[l]
                l += 1
            else:
                arr[k] = right[r]
                r+= 1

            k += 1

        while(l < len(left)):
            arr[k] = left[l]
            l += 1
            k += 1
        while(r < len(right)):
            arr[k] = right[r]
            r += 1
            k += 1


    def getKeys(self,arr):
        keys = []
        for item in arr:
            keys.append(item.key)
        return keys
