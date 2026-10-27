'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

["act","cat","stop","hat"]

actions:

dict/map: {
    a:1
    c:1
    t:1
}
sort -> find in the set
'''



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKeys(st):
            cnt = [0] * 26
            for s in st:
                cnt[ord(s) - ord("a")] += 1
            return tuple(cnt)
        res = defaultdict(list)
        for st in strs:
            key = getKeys(st)
            res[key].append(st)
        ans = []
        for _, val in res.items():
            ans.append(val)
        return ans