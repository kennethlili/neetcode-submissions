class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        smap = {}
        tmap = {}
        for char in s:
            if(char not in smap):
                smap[char] = 1
            else:
                smap[char] += 1
        for cha in t:
            if(cha not in tmap):
                tmap[cha] = 1
            else:
                tmap[cha] += 1
        
        return smap == tmap
        
        