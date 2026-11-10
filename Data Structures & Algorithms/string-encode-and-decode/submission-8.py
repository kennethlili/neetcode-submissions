"""
Facts:
    We are encoding an arr of string, to string
    and we need to restore the string to the arr of string
    We know the arr can be empty to 100
    string also can be empty
    string contains any possible characters out of 256 valid ASCII characters.
Problem:
    ["Hello","World"] -> string
    "Hello,World"
    ["Hello,World"]
    5|Hello5|World

n: len(strs), m: len(all of the string)
time: encode: O(n), decode: O(m)
space: encode: O(m)
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for st in strs:
            parts.append(str(len(st)))
            parts.append("|")
            parts.append(st)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0
        lenStrArr = []
        while i < len(s):
            if s[i] != "|":
                lenStrArr.append(s[i])
                i = i + 1
            else:
                strEndIndex = i + 1  + int("".join(lenStrArr))
                res.append(s[i + 1 : strEndIndex])
                i = strEndIndex
                lenStrArr = []

        return res
