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
                length = int("".join(lenStrArr))
                res.append(s[i + 1 : i + 1 + length])
                i = i + 1 + length
                lenStrArr = []

        # def decodeHelper(i, lenStrArr):
        #     if i >= len(s):
        #         return
        #     if s[i] != "|":
        #         lenStrArr.append(s[i])

        #         decodeHelper(i + 1, lenStrArr)
        #     else:
        #         length = int("".join(lenStrArr))
        #         res.append(s[i + 1 : i + 1 + length])
        #         decodeHelper(i + 1 + length, [])
        #     return

        # decodeHelper(0, [])
        return res
