"""
facts:
    s and t
    return the shortest substring of s so that it contains every char in t (including the duplicate)
    return "" otherwise
        substring can have gap
        any ordering is good
    char contain upper and lowercase char
    {X:1, Y:1, Z:1}
    O(m+ n^2)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ans = 0, 0  # left,right
        res_len = float("inf")

        t_lookup = defaultdict(int)
        for ch in t:
            t_lookup[ch] += 1
            
        left = 0
        curr_dict = defaultdict(int)
        needed = len(t_lookup)
        matches = 0
        for r, ch in enumerate(s):
            curr_dict[ch] += 1
            if t_lookup[ch] > 0 and curr_dict[ch] == t_lookup[ch]:
                matches += 1

            while matches == needed:
                if r - left + 1 < res_len:
                    res_len = r - left + 1
                    ans = left, r
                if t_lookup[s[left]] > 0 and curr_dict[s[left]] == t_lookup[s[left]]:
                    matches -= 1

                curr_dict[s[left]] -= 1
                left += 1

        return "" if res_len == float("inf") else s[ans[0] : ans[1] + 1]
