"""
2-9
each digit represent 3/4 eng letter
return all the possible letter combination the digits could represent
    in any order
in each combination,
    we know the len of the result == len(digits)
    could have 3/4 representing letter
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def helper(i, curr):
            if i >= len(digits):
                res.append("".join(curr))
                return
            for ch in lookup[digits[i]]:
                curr.append(ch)
                helper(i + 1, curr)
                curr.pop()

        helper(0, [])
        return res
