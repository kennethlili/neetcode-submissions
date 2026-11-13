"""
s1 and s2, return true if s2 contains a permutation of s1, false otherwise
permutation == exact same char, can be different in order but must have no gap
s1 and s2 1 <= s1.length, s2.length <= 10000
    s1 and s2 not sorted
    Both strings only contain lowercase letters
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isFinished(lookup, currSet):
            for key, val in lookup.items():
                if key not in currSet:
                    return False
                if currSet[key] != lookup[key]:
                    return False
            return True

        s1_lookup = defaultdict(int)
        for ch in s1:
            s1_lookup[ch] += 1
        j = 0
        tmp_lookup = defaultdict(int)
        for i in range(len(s2)):
            tmp_lookup[s2[i]] += 1
            if i - j + 1 > len(s1):
                tmp_lookup[s2[j]] -= 1
                j += 1

            if isFinished(s1_lookup, tmp_lookup):
                return True
        return False
