class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l = 0
        last = None # 'greater', 'less', 'equal'
        def getComparsion(r):
            if arr[r] < arr[r-1]:
                return 'greater'
            elif arr[r] > arr[r-1]:
                return 'less'
            else:
                return 'equal'
        for r in range(1, len(arr), 1):
            print(res)
            curr = getComparsion(r)
            if curr == 'equal':
                last = None
                l = r
            else:
                if not last:
                    last = curr
                    res = max(res, r-l +1)
                else:
                    if(last == 'greater' and curr == 'less') or (last == 'less' and curr == 'greater'):
                        res = max(res, r-l +1)
                        last = curr
                    else:
                        last = curr
                        l = r-1
                    

        return res