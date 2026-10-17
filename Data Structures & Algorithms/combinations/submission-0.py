class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, currarr):
            if len(currarr) == k:
                res.append(currarr.copy())
                return
            if i > n:
                return
            for j in range(i+1, n+1, 1):
                currarr.append(j)
                helper(j,currarr)
                currarr.pop()
            
        helper(0,[])
        return res