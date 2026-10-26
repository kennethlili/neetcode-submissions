"""
You are given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.


Input: str1 = "abac", str2 = "cabd"
str1 -> i
str2 -> j

check if str are equal:

==:
    i+1, j+1, add any of the str into the res
!=:
    a vs c
    2 branches:
        - i +1,j , add i str to the res
            -abac
            -cab
            -abac
        - i, j+1, add j str to the res
            -ab
            -cab
            - cabac
    base case:
        if any one of the pointer reach the end, we will push the remaing item to the res
"""

"""
Bounds:
    i : [0,len(str1)]
    j: [0, len(str2)]


"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        I,J = len(str1), len(str2)
        prev = [""] * (J + 1) 

        for i in range(I, -1, -1):
            curr = [""] * (J + 1) 
            for j in range(J, -1, -1):
                if i >= len(str1):
                    curr[j] = str2[j::]
                    continue
                if j >= len(str2):
                    curr[j] = str1[i::]
                    continue

                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j+1]
                else:
                    movei = str1[i] + prev[j]
                    movej = str2[j] + curr[j+1]
                    if len(movei) < len(movej):
                        curr[j] += movei
                    else:
                        curr[j] += movej
            prev = curr

        return prev[0]
