"""
facts:
    string s, only uppercase eng char
        string is not sorted, in any order
    We can change up to k char in string and return the longest substring that contain no duplicated char
    string 1 <= s.length <= 100,000

time: O(n^2) -> O(n)
space: O(n)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        i, j = 0, 0
        lookup = defaultdict(int)
        max_freq = 0
        while j < len(s):
            
            lookup[s[j]] += 1
            max_freq = max(max_freq, lookup[s[j]])
            # for n, freq in lookup.items():
            #     max_freq = max(max_freq, freq)
            # isValid = (j - i + 1) - max_freq <= k
            # if isValid:
            #     res = max((j - i + 1), res)
            # else:
            while (j - i + 1) - max_freq > k:
                # if lookup[s[i]] == max_freq:
                #     max_freq -= 1
                lookup[s[i]] -= 1
                # for n, freq in lookup.items():
                #     max_freq = max(max_freq, freq)
                i += 1
            res = max((j - i + 1), res)
            j += 1

        return res
