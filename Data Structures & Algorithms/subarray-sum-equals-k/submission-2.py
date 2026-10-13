class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefMap = {0: 1}
        prevSum = 0
        res = 0
        for n in nums:
            curr = prevSum + n
            prevSum = curr
            diff = curr- k
            if diff in prefMap:
                res += prefMap[diff]
            prefMap[curr] = prefMap.get(curr, 0) + 1
        
        return res