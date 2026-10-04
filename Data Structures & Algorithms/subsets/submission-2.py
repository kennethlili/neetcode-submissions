class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def helper(num):
            copyRes = res[::]
            for arr in copyRes:
                copy = arr[::]
                copy.append(num)
                res.append(copy)
        
        for num in nums:
            helper(num)

        return res