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
        # res = set()
        res = []

        def helper(i, curr, remaining):
            if remaining == 0:
                res.append(curr[:])
                return
            if remaining < 0 or i >= len(candidates):
                return
            if i != len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                tmp = i
                while tmp != len(candidates) - 1 and candidates[tmp] == candidates[tmp + 1]:
                    tmp += 1
                numsOfDuplicated = tmp - i + 1
                n = candidates[i]
                for i in range(1, numsOfDuplicated + 1):
                    helper(tmp + 1, curr + ([n] * i), remaining - (n * i))
                
                skip = helper(tmp + 1, curr, remaining)
            else:
                skip = helper(i + 1, curr, remaining)
                n = candidates[i]
                take = helper(i + 1, curr + [n], remaining - n)

        helper(0, [], target)

        # return [list(item) for item in res]
        return res
