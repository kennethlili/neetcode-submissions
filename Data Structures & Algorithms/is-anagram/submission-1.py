class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        smap = self.getMap(s)
        tmap = self.getMap(t)
        
        return smap == tmap
    def getMap(self,st):
        map = {}
        for char in st:
            if(char not in map):
                map[char] = 1
            else:
                map[char] += 1
        return map
        
        