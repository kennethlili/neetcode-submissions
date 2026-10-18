class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= [[]]
        for n in nums:
            prev = []
            for arr in res:
                for i in range(len(arr) + 1):
                    copy = arr.copy()
                    copy.insert(i,n)
                    prev.append(copy)
            res = prev
        
        return res
