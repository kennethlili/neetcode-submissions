# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    def quickSortHelper(self,arr,left, right):
        if left < right:
            pivot = self.partition(arr, left,right)
            self.quickSortHelper(arr, left, pivot - 1)
            self.quickSortHelper(arr, pivot + 1, right)
        
    def partition(self,arr, left,right):
        j,i = left,left
        pivot = right
        while(j < pivot):
            if(arr[j].key < arr[pivot].key):
                arr[i], arr[j] = arr[j], arr[i]
                i  += 1
            j+=1
        arr[i], arr[pivot] = arr[pivot], arr[i]
        return i



