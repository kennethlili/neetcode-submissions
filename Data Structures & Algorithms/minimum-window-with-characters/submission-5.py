"""
s large
t large


s = "OUZODYXAZV", t = "XYZ"
l , r

actions:
not isFinished:
    -keep moving r
isFinished:
    - set the res
    - l+= 1 until the first index of string in t
        - set the res

"""
# s = "x", t = "xy"


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for ch in t:
            lookup[ch] += 1
        need, have = len(lookup), 0

        res, resLen = "", float("inf")

        l = 0
        resLookup = defaultdict(int)
        for r, ch in enumerate(s):
            if ch in lookup and resLookup[ch] < lookup[ch] and resLookup[ch] + 1 >= lookup[ch]:
                have += 1
            if ch in lookup:
                resLookup[ch] += 1

            isFinished = need == have
            if isFinished:
                currR = s[l : r + 1]
                resLen = min(resLen, len(currR))
                if resLen == len(currR):
                    res = currR
                while need == have:
                    currR = s[l : r + 1]
                    resLen = min(resLen, len(currR))
                    if resLen == len(currR):
                        res = currR
                    if s[l] in lookup:
                        resLookup[s[l]] -= 1
                        if resLookup[s[l]] < lookup[s[l]]:
                            have -= 1
                    l += 1

                    

        return res
