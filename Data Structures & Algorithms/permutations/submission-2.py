'''
nums:
    unique integher
permutations:
    [1,2]
    [1,2] [2,1]
    1: 1
    2: 2
    3: 6
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            for i,n in enumerate(nums):
                if used[i]:
                    continue
                curr.append(n)
                used[i] = True
                dfs(curr)
                curr.pop()
                used[i] = False
                
            # return res
        dfs([])
        return res