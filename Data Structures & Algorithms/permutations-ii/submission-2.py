class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnt = {}
        for n in nums:
            if n not in cnt:
                cnt[n] = 0
            cnt[n] += 1
        res = []
        perm = []
        def dfs():
            if len(perm) == len(nums):
                copy = perm.copy()
                res.append(copy)
                return
            for n in cnt:
                if cnt[n] > 0:
                    perm.append(n)
                    cnt[n] -= 1
                    dfs()
                    perm.pop()
                    cnt[n] += 1
        
        dfs()
        return res

