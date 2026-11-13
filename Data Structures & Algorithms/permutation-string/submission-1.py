'''
s1 and s2, return true if s2 contains a permutation of s1, false otherwise
permutation == exact same char, can be different in order but must have no gap
s1 and s2 1 <= s1.length, s2.length <= 10000
    s1 and s2 not sorted
    Both strings only contain lowercase letters
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isFinished(lookup):
            for n in lookup.values():
                if n != 0: return False
            return True
        # for i in range(s1)
        s1_lookup = defaultdict(int)
        for ch in s1:
            s1_lookup[ch] += 1
        # for i, ch in enumerate(s2):
        #     if ch in s1_lookup:
        for i in range(len(s2)):
            s1_lookup_copy = s1_lookup.copy()
            while i < len(s2) and s2[i] in s1_lookup_copy:
                s1_lookup_copy[s2[i]] -= 1
                if s1_lookup_copy[s2[i]] < 0:
                    break
                if isFinished(s1_lookup_copy):
                    return True
                i += 1
        return False

