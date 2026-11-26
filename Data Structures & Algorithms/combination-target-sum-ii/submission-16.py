"""
candidates arr contains integers
    may contains duplicates
    candidates is not sorted
target integers
find the subset of candidates which. sum up to target
    we can return in any order
    can only choose element from candidates at most once within a combination
    the solution set must not contain duplicate combination
take 1
take 2
skip 2

take 1
skip 2
take 2

take1
take2
take2
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(i, curr, remaining):
            if remaining == 0:
                res.append(curr)
                return
            if remaining < 0 or i >= len(candidates):
                return
            if i != len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                newi = i
                while newi != len(candidates) - 1 and candidates[newi] == candidates[newi + 1]:
                    newi += 1
                newi += 1
                numsOfDuplicated = newi - i 
                n = candidates[i]
                for i in range(1, numsOfDuplicated + 1):
                    helper(newi , curr + ([n] * i), remaining - (n * i))
                helper(newi , curr, remaining)
            else:
                helper(i + 1, curr, remaining)
                n = candidates[i]
                helper(i + 1, curr + [n], remaining - n)

        helper(0, [], target)

        return res
