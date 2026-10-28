class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = set()
        for n in nums:
            if n not in cnt:
                cnt.add(n)
            else:
                return True
        
        return False