"""
s1 and s2, return true if s2 contains a permutation of s1, false otherwise
permutation == exact same char, can be different in order but must have no gap
s1 and s2 1 <= s1.length, s2.length <= 10000
    s1 and s2 not sorted
    Both strings only contain lowercase letters
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_lookup = defaultdict(int)
        for ch in s1:
            s1_lookup[ch] += 1
        j = 0
        tmp_lookup = defaultdict(int)
        matches = 0
        target = len(s1_lookup)
        for i in range(len(s2)):
            tmp_lookup[s2[i]] += 1
            if tmp_lookup[s2[i]] == s1_lookup[s2[i]]:
                matches +=1
            elif tmp_lookup[s2[i]] == s1_lookup[s2[i]] + 1:
                matches -=1
            if i - j + 1 > len(s1):
                if tmp_lookup[s2[j]] == s1_lookup[s2[j]] + 1:
                    matches += 1
                elif tmp_lookup[s2[j]] == s1_lookup[s2[j]]:
                    matches -= 1
                tmp_lookup[s2[j]] -= 1

                j += 1

            if i - j + 1 == len(s1) and matches == target:
                return True
        return False
