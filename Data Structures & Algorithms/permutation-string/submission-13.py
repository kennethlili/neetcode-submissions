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
        target = len(s1_lookup)
        left = 0
        curr = defaultdict(int)
        matches = 0
        for r in range(len(s2)):
            window_size = r- left + 1
            
            curr[s2[r]] += 1
            if curr[s2[r]] == s1_lookup[s2[r]]:
                matches += 1
            elif curr[s2[r]] == s1_lookup[s2[r]] +1:
                matches -= 1
            if window_size > len(s1):
                if curr[s2[left]] == s1_lookup[s2[left]]:
                    matches -= 1
                elif curr[s2[left]] == s1_lookup[s2[left]] + 1:
                    matches += 1    
                curr[s2[left]] -= 1
               
                left += 1
            if matches == target:
                return True
        return False




