"""
facts:
    anagram is a string that contains the exact same chars without order
    arr of strs, group all anagrams together into a sublists
        any order is fine
        is not sorted
    arr of the str 1 <= strs.length <= 10000
    str can be empty,0 <= strs[i].length <= 100
    only contains lower case eng char

how do we avoid processed string
set() -> stored all the process string index

what defined an anagram?
    their char must be the exact
    act act
n ->total char we have
O(n^2) -> O(m * nlogn)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        res = []

        for st in strs:
            cnt = [0] * 26
            for ch in st:
                ch_id = ord(ch) - ord('a')
                cnt[ch_id] += 1
            lookup[tuple(cnt)].append(st)

            # sst = "".join(sorted(st))
            # lookup[sst].append(st)
        for key, val in lookup.items():
            res.append(val)
        return res

            