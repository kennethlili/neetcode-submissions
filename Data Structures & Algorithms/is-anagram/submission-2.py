class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = defaultdict(int)
        for charS in s:
            cnt[charS] += 1
        for charT in t:
            cnt[charT] -= 1
            if cnt[charT] == 0:
                cnt.pop(charT)
        return len(cnt) == 0