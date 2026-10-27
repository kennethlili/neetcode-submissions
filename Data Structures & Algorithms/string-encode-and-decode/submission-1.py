'''
Encode an arr of strieng

then decode it after

"als&"
"5&s1*"

004als& 0055&s1*
strlen: 4
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            prefix = str(len(st))
            if len(prefix) == 1:
                prefix = "00" + prefix
            if len(prefix) == 2:
                prefix = '0' + prefix
            setSt = prefix+ st
            res += setSt
        return res
            

    def decode(self, s: str) -> List[str]:
        res = []
        def helper(start):
            if start >= len(s):
                return
            strLen = int(s[start:start+3])
            targetSt = s[start+ 3: start+ 3+ strLen ]
            res.append(targetSt)
            nextStart = start + 3 + strLen
            helper(nextStart)

            
        helper(0)
        return res



