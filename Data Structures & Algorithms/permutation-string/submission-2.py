'''
s1 and s2, return true if s2 contains a permutation of s1, false otherwise
permutation == exact same char, can be different in order but must have no gap
s1 and s2 1 <= s1.length, s2.length <= 10000
    s1 and s2 not sorted
    Both strings only contain lowercase letters
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isFinished(lookup, currSet):
            for key, val in lookup.items():
                if key not in currSet : return False
                if currSet[key] != lookup[key]: return False
            return True
        s1_lookup = defaultdict(int)
        for ch in s1:
            s1_lookup[ch] += 1
        
        # for i in range(len(s2)):
            
            # look for the char in s1 in s2 to meet the char with no gap
            # while i < len(s2) and s2[i] in s1_lookup_copy:
            #     s1_lookup_copy[s2[i]] -= 1
            #     if s1_lookup_copy[s2[i]] < 0:
            #         break
            #     if isFinished(s1_lookup_copy):
            #         return True
            #     i += 1
        j = 0
        tmp_lookup = defaultdict(int)
        for i in range(len(s2)):
            window_size = i -j + 1
            ch = s2[i]
            tmp_lookup[ch] += 1

            if window_size == len(s1):
                if isFinished(s1_lookup, tmp_lookup): return True
            elif window_size  >len(s1):
                tmp_lookup[s2[j]] -= 1
                # if tmp_lookup[s2[j]] == 0:
                #     del tmp_lookup[s2[j]]
                j += 1

                if isFinished(s1_lookup, tmp_lookup): return True
        return False



            




        return False

