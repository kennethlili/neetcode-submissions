'''
length = large

zxyzxyz

cnt:{} key: char, val : index.
z,x,y,z

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cnt = {}
        l = 0
        for i,ch in enumerate(s):
            
            if ch in cnt:
                l = max(l, cnt[ch] + 1)
            cnt[ch] = i
            res = max(res, i-l + 1)


                
        return res