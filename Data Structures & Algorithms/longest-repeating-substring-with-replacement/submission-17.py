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
        curr = defaultdict(int)
        res = 0
        left = 0
        mostFreq = 0
        for r in range(len(s)):
            ch = s[r]
            curr[ch] += 1
            mostFreq = max(mostFreq, curr[ch])
            # for n, freq in curr.items():
            #     mostFreq = max(mostFreq, freq)
            while not ((r - left + 1) - mostFreq <= k):
                curr[s[left]] -= 1
                
                left += 1
            res = max(res, r - left + 1)

        return res
