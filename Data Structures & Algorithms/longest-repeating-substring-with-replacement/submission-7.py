'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.


actions:
l reference

cnt defaultdict(int)
iterate r
len = r - l + 1
check len - mostfreqNumber <= k
    - yes, push to the res
    - no, move l until valid, and remove the l number meanwhile
if r at the end


iterate the i in s


'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        l = 0
        # O(1)
        def getMostFreqNum():
            ans = 0
            for _, freq in cnt.items():
                ans= max(ans, freq)
            return ans

        for r, ch in enumerate(s):
            cnt[ch] += 1
            length = r- l + 1
            freq = getMostFreqNum()
            diff = length - freq
            if diff <= k:
                res = max(res, length)
            else:
                while ((r- l + 1) - getMostFreqNum()) > k:
                    cnt[s[l]] -= 1
                    l += 1
        
        return res
