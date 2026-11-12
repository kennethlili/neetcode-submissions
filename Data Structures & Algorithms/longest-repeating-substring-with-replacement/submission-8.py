"""
facts:
    string s, only uppercase eng char
        string is not sorted, in any order
    We can change up to k char in string and return the longest substring that contain no duplicated char
    string 1 <= s.length <= 100,000

time: O(n^2)
space: O(n)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        # for i in range(len(s)):
        #     ref = None
        #     lookup = defaultdict(int)
        #     lookup[s[i]] += 1
        #     if lookup[s[i]] > k:
        #         ref = s[i]
        #     # find the maximum len that allow k different char
        #     for j in range(i+1, len(s)):
        #         lookup[s[j]] += 1
        #         if lookup[s[j]] > k:
        #             if not ref:
        #                 ref = s[j]
        #             elif ref != s[j]:
        #                 break
        #         res = max(res, j - i + 1)
                
        # return res
        # if len(s) == 1:
        #     return 1
        i, j = 0, 0
        lookup = defaultdict(int)
        while(j < len(s)):
            lookup[s[j]] += 1
            max_freq = 0
            for n, freq in lookup.items():
                max_freq = max(max_freq, freq)
            windLen = (j- i + 1)
            isValid = windLen - max_freq <= k
            if isValid:
                res = max(windLen, res)
            else:
                while (j- i + 1) - max_freq > k:
                    lookup[s[i]] -= 1
                    for n, freq in lookup.items():
                        max_freq = max(max_freq, freq)
                    i += 1
            j+=1
            
        return res

            

                

