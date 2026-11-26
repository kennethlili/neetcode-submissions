"""
integer n
well-formed parentheses string with n pairs of parentheses
    it contains n of ()
    all open and close bracket must be close properly
    # of ( == # of ) == n
    all len must be equal to n * 2
    each index, we insert only ( or )
    in order for us to insert ), we need closeRemain > openRemain


1:
()
2:
()()
(())
3:
()()()
(()))
(()())
()(())
((()))
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, openRemain, closeRemain):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            if openRemain -1  >= 0:
                curr.append("(")
                insrtOpen = backtrack(curr , openRemain - 1, closeRemain)
                curr.pop()
            if closeRemain -1  >= 0 and closeRemain > openRemain:
                curr.append(")")
                insrtClose = backtrack(curr , openRemain, closeRemain - 1)
                curr.pop()

        backtrack([], n,n)
        return res
