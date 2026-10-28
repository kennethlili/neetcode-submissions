'''
You may return the output in any order.

strs len big
str size small


strs = ["act","pots","tops","cat","stop","hat"]

map = {
(act):1
}
sort the string


each char represent a number/id
ord(char) - ord('a')

[0]* 26



'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cntMap = defaultdict(list)
        res = []
        for st in strs:
            stid = [0]* 26
            for char in st:
                stid[ord(char) - ord('a')] += 1
            cntMap[tuple(stid)].append(st)
        for _, val in cntMap.items():
            res.append(val)
        return res
