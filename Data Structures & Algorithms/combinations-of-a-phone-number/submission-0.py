class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
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
            if len(curr) == len(digits):
                copy = curr
                res.append(copy)
                return
            if i >= len(digits):
                return

            chars = digitToChar[digits[i]]
            for char in chars:
                curr = curr + char
                helper(i + 1, curr)
                curr = curr[:-1]
        if digits:
            helper(0, "")
        return res
