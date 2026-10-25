"""
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.
- get the lcs
- return 0 if not exist

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".

A common subsequence of two strings is a subsequence that exists in both strings.

summary: get lcs of 2 texts
-both texts are defined, so we dont need to check edge case where text1 or text2 doesnt have anything
- text1 and text2 consist of only lowercase English characters.
    - we just need to ==, no need any converation

Input: text1 = "cat", text2 = "crabt"


Actions:
text1 - > i, text2 -> j
i = 0, j = 0 ->they are equal -> +1 -> add both i and j pter
i = 1, j= 1 -> !=
-> keeping i constant, increase j
-> keeping j constant, increase i

found -> increase i and j
not found,

base case:
if anyone of the pter out of bound (len(text)) -> return
"""

"""
Bounds:
    i: [0, len(text1)]
    j: [0, len(text2)]
    both positive, use arr to index


"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bounds:
        #     i: [0, len(text1)]
        #     j: [0, len(text2)]
        #     both positive, use arr to index

        # Order:
        #     equal str:
        #         both increasing value, i and j
        #         big before small

        dp = [[None] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in range(len(text1), -1, -1):
            for j in range(len(text2), -1, -1):
                if i >= len(text1) or j >= len(text2):
                    dp[i][j] = 0
                    continue

                best = 0
                if text1[i] == text2[j]:
                    best = 1 + dp[i + 1][j + 1]

                else:
                    movei = dp[i + 1][j]
                    movej = dp[i][j + 1]
                    best = max(movei, movej)
                dp[i][j] = best
        return dp[0][0]
