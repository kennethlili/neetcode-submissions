# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if(not pairs):
            return []
        res = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1
            while(pairs[j+1].key < pairs[j].key) and j >= 0:
                pairs[j], pairs[j + 1] = pairs[j+1], pairs[j]
                j -= 1
            res.append(pairs[:])
            i +=1

        return res