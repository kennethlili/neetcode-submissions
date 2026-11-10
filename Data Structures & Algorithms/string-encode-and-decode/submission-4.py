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
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            prefix = str(len(st)) + '|'
            res += (prefix + st)
        return res
    def decode(self, s: str) -> List[str]:
        # if not s:
        #     return []
        res = []
        def decodeHelper(i,lenStr):
            if i >= len(s):
                return
            if s[i] != "|":
                decodeHelper(i+1, lenStr + s[i])
            else:
                length = int(lenStr)
                res.append(s[i+1: i+1 + length])
                decodeHelper(i+1 + length,"")
            return
        decodeHelper(0,"")
        return res
            